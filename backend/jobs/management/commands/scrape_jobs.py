import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from jobs.models import Job
from django.utils import timezone


class Command(BaseCommand):
    help = "Scrape jobs from Djinni with customizable parameters."

    def add_arguments(self, parser):
        parser.add_argument(
            "--keyword", type=str, help="Filter by keyword (e.g. Python)"
        )
        parser.add_argument(
            "--location", type=str, help="Filter by location (e.g. Kyiv, remote)"
        )

    def handle(self, *args, **options):
        keyword = options.get("keyword", "")
        location = options.get("location", "")

        base_url = "https://djinni.co/jobs/"
        query_params = []

        if keyword:
            query_params.append(f"primary_keyword={keyword}")
        if location:
            query_params.append(f"location={location}")

        full_url = base_url + "?" + "&".join(query_params) if query_params else base_url
        self.stdout.write(f"Scraping jobs with URL: {full_url}")

        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(full_url, headers=headers)
        if response.status_code != 200:
            self.stderr.write(f"Failed to fetch data: {response.status_code}")
            return

        # print(
        #     response.text[:1000]
        # )  # Debugging line to print first 1000 characters of the response

        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.find_all("li", id=lambda x: x and x.startswith("job-item-"))
        if not job_cards:
            self.stderr.write(
                "No job cards found. The page structure may have changed or you are being blocked."
            )

        self.stdout.write(f"Found {len(job_cards)} job listings")
        new_jobs = 0

        for card in job_cards:
            title_tag = card.find("a", class_="job-item__title-link")
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            job_url = "https://djinni.co" + title_tag["href"]

            company_elem = card.find("a", attrs={"data-analytics": "company_page"})
            company = company_elem.get_text(strip=True) if company_elem else None

            salary_elem = card.find("span", class_="public-salary-item")
            salary = salary_elem.get_text(strip=True) if salary_elem else None

            location_elem = card.find("span", class_="location-text")
            location_text = (
                location_elem.get_text(strip=True) if location_elem else None
            )

            experience = None
            for span in card.find_all("span", class_="text-nowrap"):
                if "досвіду" in span.get_text():
                    experience = span.get_text(strip=True)
                    break

            experience = experience or None
            try:
                obj, created = Job.objects.update_or_create(
                    url=job_url,
                    defaults={
                        "title": title,
                        "company": company,
                        "salary": salary,
                        "location": location_text,
                        "experience": experience,
                        "description": f"Scraped from Djinni with keyword: {keyword}, location: {location}",
                        "source": "djinni",
                        "date_published": timezone.now(),
                        "is_active": True,
                    },
                )
                if created:
                    new_jobs += 1
                    self.stdout.write(f"Saved job: {title}")
            except Exception as e:
                self.stderr.write(f"Error saving job '{title}': {e}")

        self.stdout.write(f"Total new jobs added: {new_jobs}")
