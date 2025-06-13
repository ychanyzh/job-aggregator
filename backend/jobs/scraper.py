import requests
from bs4 import BeautifulSoup
from .models import Job

BASE_URL = "https://djinni.co"


def fetch_jobs(keyword: str):
    """Scrape Djinni jobs filtered by keyword"""
    url = f"{BASE_URL}/jobs/"
    params = {"primary_keyword": keyword}
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for title_tag in soup.select("a.job-item__title-link"):
        job_url = BASE_URL + title_tag["href"]
        job_title = title_tag.get_text(strip=True)

        job_card = title_tag.find_parent("h2").find_next_sibling("div")
        location_tag = job_card.select_one(".location-text")
        experience_tag = job_card.find_all("span", class_="text-nowrap")[-1]

        description_tag = soup.select_one(
            f'div[id="job-description-{title_tag["href"].split("/")[-2]}"] span'
        )

        jobs.append(
            {
                "title": job_title,
                "url": job_url,
                "location": location_tag.get_text(strip=True) if location_tag else "",
                "experience": (
                    experience_tag.get_text(strip=True) if experience_tag else ""
                ),
                "description": (
                    description_tag.get_text(strip=True) if description_tag else ""
                ),
            }
        )

    return jobs
