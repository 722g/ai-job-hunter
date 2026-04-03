import requests
from config import SERPAPI_KEY

def search_jobs(keywords, location="", num_results=10):
    jobs = []
    jobs += search_serpapi(keywords, location, num_results)
    jobs += search_hrge(keywords)
    jobs += search_jobsge(keywords)
    jobs += search_linkedin(keywords, location)
    jobs += search_vacancies_ge(keywords)
    seen = set()
    unique_jobs = []
    for job in jobs:
        key = job["title"] + job["company"]
        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)
    return unique_jobs


def search_serpapi(keywords, location="", num_results=10):
    jobs = []
    for keyword in keywords[:3]:
        query = f"{keyword} {location}" if location else keyword
        params = {
            "engine": "google_jobs",
            "q": query,
            "api_key": SERPAPI_KEY,
            "num": num_results
        }
        try:
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            data = response.json()
            if "jobs_results" in data:
                for job in data["jobs_results"]:
                    apply_options = job.get("apply_options", [])
                    link = apply_options[0].get("link", "#") if apply_options else job.get("share_link", "#")
                    jobs.append({
                        "title": job.get("title", ""),
                        "company": job.get("company_name", ""),
                        "location": job.get("location", ""),
                        "description": job.get("description", "")[:500],
                        "via": job.get("via", ""),
                        "link": link,
                        "posted": job.get("detected_extensions", {}).get("posted_at", ""),
                        "source": "Google Jobs"
                    })
        except Exception as e:
            print(f"SerpAPI error: {e}")
    return jobs


def search_hrge(keywords):
    jobs = []
    for keyword in keywords[:2]:
        try:
            params = {
                "engine": "google",
                "q": f"{keyword} site:hr.ge",
                "api_key": SERPAPI_KEY,
                "num": 5
            }
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            data = response.json()
            for result in data.get("organic_results", []):
                title = result.get("title", "").replace(" - hr.ge", "").strip()
                link = result.get("link", "#")
                snippet = result.get("snippet", "")
                if title and len(title) > 3:
                    jobs.append({
                        "title": title,
                        "company": "See on hr.ge",
                        "location": "Tbilisi, Georgia",
                        "description": snippet,
                        "via": "hr.ge",
                        "link": link,
                        "posted": "",
                        "source": "hr.ge"
                    })
        except Exception as e:
            print(f"hr.ge error: {e}")
    return jobs


def search_jobsge(keywords):
    jobs = []
    for keyword in keywords[:2]:
        try:
            params = {
                "engine": "google",
                "q": f"{keyword} site:jobs.ge",
                "api_key": SERPAPI_KEY,
                "num": 5
            }
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            data = response.json()
            for result in data.get("organic_results", []):
                title = result.get("title", "").replace(" - jobs.ge", "").strip()
                link = result.get("link", "#")
                snippet = result.get("snippet", "")
                if title and len(title) > 3:
                    jobs.append({
                        "title": title,
                        "company": "See on jobs.ge",
                        "location": "Tbilisi, Georgia",
                        "description": snippet,
                        "via": "jobs.ge",
                        "link": link,
                        "posted": "",
                        "source": "jobs.ge"
                    })
        except Exception as e:
            print(f"jobs.ge error: {e}")
    return jobs


def search_linkedin(keywords, location=""):
    jobs = []
    for keyword in keywords[:2]:
        try:
            query = f"{keyword} site:linkedin.com/jobs"
            if location:
                query += f" {location}"
            params = {
                "engine": "google",
                "q": query,
                "api_key": SERPAPI_KEY,
                "num": 5
            }
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            data = response.json()
            for result in data.get("organic_results", []):
                title = result.get("title", "").replace(" | LinkedIn", "").strip()
                link = result.get("link", "#")
                snippet = result.get("snippet", "")
                if title and len(title) > 3:
                    jobs.append({
                        "title": title,
                        "company": "See on LinkedIn",
                        "location": location if location else "Remote / Various",
                        "description": snippet,
                        "via": "LinkedIn",
                        "link": link,
                        "posted": "",
                        "source": "LinkedIn"
                    })
        except Exception as e:
            print(f"LinkedIn error: {e}")
    return jobs


def search_vacancies_ge(keywords):
    jobs = []
    for keyword in keywords[:2]:
        try:
            params = {
                "engine": "google",
                "q": f"{keyword} site:vacancies.ge",
                "api_key": SERPAPI_KEY,
                "num": 5
            }
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            data = response.json()
            for result in data.get("organic_results", []):
                title = result.get("title", "").replace(" - vacancies.ge", "").replace(" | vacancies.ge", "").strip()
                link = result.get("link", "#")
                snippet = result.get("snippet", "")
                if title and len(title) > 3:
                    jobs.append({
                        "title": title,
                        "company": "See on vacancies.ge",
                        "location": "Tbilisi, Georgia",
                        "description": snippet,
                        "via": "vacancies.ge",
                        "link": link,
                        "posted": "",
                        "source": "vacancies.ge"
                    })
        except Exception as e:
            print(f"vacancies.ge error: {e}")
    return jobs


def filter_jobs_by_location(jobs, candidate_location):
    if not candidate_location:
        return jobs
    candidate_location = candidate_location.lower()
    location_keywords = candidate_location.replace("(utc+4)", "").replace("(utc+3)", "").strip().split(",")
    location_keywords = [l.strip() for l in location_keywords]
    relevant = []
    for job in jobs:
        job_location = job["location"].lower()
        job_title = job["title"].lower()
        if any(word in job_location for word in ["remote", "anywhere", "worldwide"]):
            job["location"] = "🌍 Remote"
            relevant.append(job)
            continue
        if any(loc in job_location for loc in location_keywords if loc):
            relevant.append(job)
            continue
        if "remote" in job_title:
            relevant.append(job)
            continue
    if not relevant:
        return jobs
    return relevant