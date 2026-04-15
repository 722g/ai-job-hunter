import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY

COUNTRY_MAP = {
    "English": "gb",
    "German": "de",
    "Russian": "gb",
    "Polish": "pl"
}

def search_jobs(keywords, language="English", results=20):
    country = COUNTRY_MAP.get(language, "gb")
    
    try:
        url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
        params = {
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "results_per_page": results,
            "what": keywords,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        jobs = []
        for job in data.get("results", []):
            jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company", {}).get("display_name", ""),
                "location": job.get("location", {}).get("display_name", ""),
                "description": job.get("description", ""),
                "url": job.get("redirect_url", ""),
                "salary_min": job.get("salary_min", ""),
                "salary_max": job.get("salary_max", ""),
            })
        return jobs
    except Exception as e:
        print(f"Adzuna API error: {e}")
        return []
