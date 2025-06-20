# Job Radar

A simple job aggregator built with Django, DRF, and React. Scrapes job listings from Djinni.co and provides an API + web UI for browsing, filtering, and searching job opportunities.

## Features

- ✅ Job scraping from Djinni.co
- ✅ Filter, search and sort vacancies
- ✅ API with pagination, filtering, and search
- ✅ Frontend in React (Vite)

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-name/job-radar.git
cd job-radar

# 2. Build and run docker containers
docker compose up --build
```

Then open:

- Backend API: http://localhost:8000/api/jobs/
- Frontend App: http://localhost:3000

## Scraping Jobs

```bash
# Run scraper with a keyword (e.g., Python)
docker compose run backend python manage.py scrape_jobs --keyword=Python
```

You can also filter by location:

```bash
docker compose run backend python manage.py scrape_jobs --keyword=Python --location=remote
```

## Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- Postgres (via Docker)
- React + Vite

## License

MIT