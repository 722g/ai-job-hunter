import os
import anthropic
import tempfile
from datetime import date
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, ANTHROPIC_API_KEY, MODEL
from modules.cv_parser import extract_text_from_file, parse_cv_with_claude
from modules.job_search import search_jobs, filter_jobs_by_location
from modules.writer import generate_cover_letter, generate_application_answer

app = Flask(__name__)
app.secret_key = "primo-ai-job-hunter-secret-2024-xK9mP2qL"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = tempfile.gettempdir()
app.config['SESSION_PERMANENT'] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
Session(app)

DAILY_LIMIT = 10

def check_limit(action):
    today = str(date.today())
    if session.get("limit_date") != today:
        session["limit_date"] = today
        session["cv_count"] = 0
        session["cover_count"] = 0
        session["answer_count"] = 0
    return session.get(f"{action}_count", 0) < DAILY_LIMIT

def increment_limit(action):
    session[f"{action}_count"] = session.get(f"{action}_count", 0) + 1
    session.modified = True

def get_cv_data():
    return {
        "full_name": session.get("cv_name", ""),
        "email": session.get("cv_email", ""),
        "skills": session.get("cv_skills", []),
        "experience_years": session.get("cv_experience", ""),
        "summary": session.get("cv_summary", ""),
        "education": session.get("cv_education", ""),
    }

def clean_text(text):
    import re
    text = re.sub(r'#{1,6}\s*', '', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'---+', '', text)
    text = re.sub(r'___+', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

TRANSLATIONS = {
    "English": {
        "subtitle": "Upload your CV. Get matched jobs, cover letters, and answers.",
        "upload_cv": "Upload CV", "manual_search": "Manual Search",
        "drop_cv": "Drop your CV here", "file_types": "PDF or DOCX · Max 5MB",
        "no_file": "No file chosen", "extract_btn": "Extract Skills & Find Jobs",
        "search_jobs_btn": "Search Jobs", "job_title_placeholder": "Job title e.g. QA Engineer, Python Developer",
        "location_placeholder": "Location e.g. Tbilisi, Remote", "analyzing": "Analyzing your CV with Claude AI...",
        "searching": "Searching jobs...", "skill_extraction": "Skill extraction",
        "live_results": "Live job results", "cover_letters": "Cover letters",
        "job_results": "Job Results", "real_vacancies": "Real vacancies matched to your profile",
        "filter_location": "Filter by location e.g. Remote, Tbilisi...", "search": "Search",
        "new_cv": "New CV", "jobs_found": "jobs found", "apply": "Apply →",
        "cover_letter": "Cover Letter", "back_to_jobs": "← Back to Jobs",
        "ai_generated": "AI-generated based on your CV", "job_details": "Job Details",
        "job_title": "Job title", "company": "Company name",
        "job_desc_placeholder": "Paste job description here (optional but recommended)...",
        "generate_cover": "Generate Cover Letter", "generating": "Generating cover letter...",
        "copy": "Copy", "back_to_jobs_btn": "← Back to Jobs",
        "answer_question": "Answer Application Question",
        "question_placeholder": "Paste application question here...",
        "generate_answer": "Generate Answer", "generating_answer": "Generating answer...",
        "no_jobs": "No jobs found", "no_jobs_sub": "Try different keywords or remove location filter",
        "back": "← Back", "application_answer": "Application Answer",
    },
    "German": {
        "subtitle": "Laden Sie Ihren Lebenslauf hoch. Erhalten Sie passende Jobs, Anschreiben und Antworten.",
        "upload_cv": "Lebenslauf hochladen", "manual_search": "Manuelle Suche",
        "drop_cv": "Lebenslauf hier ablegen", "file_types": "PDF oder DOCX · Max 5MB",
        "no_file": "Keine Datei ausgewählt", "extract_btn": "Fähigkeiten extrahieren & Jobs finden",
        "search_jobs_btn": "Jobs suchen", "job_title_placeholder": "Berufsbezeichnung z.B. QA-Ingenieur",
        "location_placeholder": "Ort z.B. Berlin, Remote", "analyzing": "Lebenslauf wird analysiert...",
        "searching": "Jobs werden gesucht...", "skill_extraction": "Fähigkeiten",
        "live_results": "Live-Ergebnisse", "cover_letters": "Anschreiben",
        "job_results": "Jobergebnisse", "real_vacancies": "Echte Stellen für Ihr Profil",
        "filter_location": "Nach Ort filtern z.B. Remote, Berlin...", "search": "Suchen",
        "new_cv": "Neuer Lebenslauf", "jobs_found": "Jobs gefunden", "apply": "Bewerben →",
        "cover_letter": "Anschreiben", "back_to_jobs": "← Zurück zu Jobs",
        "ai_generated": "KI-generiert basierend auf Ihrem Lebenslauf", "job_details": "Jobdetails",
        "job_title": "Berufsbezeichnung", "company": "Firmenname",
        "job_desc_placeholder": "Stellenbeschreibung hier einfügen (optional aber empfohlen)...",
        "generate_cover": "Anschreiben generieren", "generating": "Anschreiben wird generiert...",
        "copy": "Kopieren", "back_to_jobs_btn": "← Zurück zu Jobs",
        "answer_question": "Bewerbungsfrage beantworten",
        "question_placeholder": "Bewerbungsfrage hier einfügen...",
        "generate_answer": "Antwort generieren", "generating_answer": "Antwort wird generiert...",
        "no_jobs": "Keine Jobs gefunden", "no_jobs_sub": "Versuchen Sie andere Stichwörter",
        "back": "← Zurück", "application_answer": "Bewerbungsantwort",
    },
    "Russian": {
        "subtitle": "Загрузите резюме. Получите вакансии, сопроводительные письма и ответы.",
        "upload_cv": "Загрузить резюме", "manual_search": "Ручной поиск",
        "drop_cv": "Перетащите резюме сюда", "file_types": "PDF или DOCX · Макс 5МБ",
        "no_file": "Файл не выбран", "extract_btn": "Извлечь навыки и найти вакансии",
        "search_jobs_btn": "Найти вакансии", "job_title_placeholder": "Должность, например QA-инженер",
        "location_placeholder": "Город, например Тбилиси, Удалённо", "analyzing": "Анализ резюме...",
        "searching": "Поиск вакансий...", "skill_extraction": "Навыки",
        "live_results": "Актуальные вакансии", "cover_letters": "Письма",
        "job_results": "Результаты поиска", "real_vacancies": "Реальные вакансии для вашего профиля",
        "filter_location": "Фильтр по городу...", "search": "Поиск",
        "new_cv": "Новое резюме", "jobs_found": "вакансий найдено", "apply": "Откликнуться →",
        "cover_letter": "Сопроводительное письмо", "back_to_jobs": "← Назад к вакансиям",
        "ai_generated": "Создано ИИ на основе вашего резюме", "job_details": "Детали вакансии",
        "job_title": "Должность", "company": "Название компании",
        "job_desc_placeholder": "Вставьте описание вакансии (необязательно)...",
        "generate_cover": "Создать письмо", "generating": "Создание письма...",
        "copy": "Копировать", "back_to_jobs_btn": "← Назад к вакансиям",
        "answer_question": "Ответить на вопрос",
        "question_placeholder": "Вставьте вопрос сюда...",
        "generate_answer": "Создать ответ", "generating_answer": "Создание ответа...",
        "no_jobs": "Вакансии не найдены", "no_jobs_sub": "Попробуйте другие ключевые слова",
        "back": "← Назад", "application_answer": "Ответ на вопрос",
    },
    "Polish": {
        "subtitle": "Prześlij swoje CV. Otrzymaj dopasowane oferty, listy motywacyjne i odpowiedzi.",
        "upload_cv": "Prześlij CV", "manual_search": "Ręczne wyszukiwanie",
        "drop_cv": "Upuść CV tutaj", "file_types": "PDF lub DOCX · Maks 5MB",
        "no_file": "Nie wybrano pliku", "extract_btn": "Wyodrębnij umiejętności i znajdź oferty",
        "search_jobs_btn": "Szukaj ofert", "job_title_placeholder": "Stanowisko np. Inżynier QA",
        "location_placeholder": "Lokalizacja np. Warszawa, Zdalnie", "analyzing": "Analizowanie CV...",
        "searching": "Wyszukiwanie ofert...", "skill_extraction": "Umiejętności",
        "live_results": "Oferty na żywo", "cover_letters": "Listy motywacyjne",
        "job_results": "Wyniki wyszukiwania", "real_vacancies": "Prawdziwe oferty dla Twojego profilu",
        "filter_location": "Filtruj według lokalizacji...", "search": "Szukaj",
        "new_cv": "Nowe CV", "jobs_found": "ofert znalezionych", "apply": "Aplikuj →",
        "cover_letter": "List motywacyjny", "back_to_jobs": "← Powrót do ofert",
        "ai_generated": "Wygenerowane przez AI na podstawie Twojego CV", "job_details": "Szczegóły oferty",
        "job_title": "Stanowisko", "company": "Nazwa firmy",
        "job_desc_placeholder": "Wklej opis stanowiska tutaj (opcjonalnie)...",
        "generate_cover": "Generuj list motywacyjny", "generating": "Generowanie listu...",
        "copy": "Kopiuj", "back_to_jobs_btn": "← Powrót do ofert",
        "answer_question": "Odpowiedz na pytanie rekrutacyjne",
        "question_placeholder": "Wklej pytanie tutaj...",
        "generate_answer": "Generuj odpowiedź", "generating_answer": "Generowanie odpowiedzi...",
        "no_jobs": "Nie znaleziono ofert", "no_jobs_sub": "Spróbuj innych słów kluczowych",
        "back": "← Powrót", "application_answer": "Odpowiedź na pytanie",
    }
}

def get_t():
    lang = session.get("language", "English")
    return TRANSLATIONS.get(lang, TRANSLATIONS["English"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def is_valid_location(location):
    if not location or len(location) <= 2:
        return True
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    result = client.messages.create(
        model=MODEL,
        max_tokens=10,
        messages=[{"role": "user", "content": f"Is '{location}' a real city or country name? Reply only YES or NO."}]
    )
    return "YES" in result.content[0].text.strip().upper()

def is_valid_job_title(query):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    result = client.messages.create(
        model=MODEL,
        max_tokens=10,
        messages=[{"role": "user", "content": f"Is '{query}' a real job title or profession? Reply only YES or NO."}]
    )
    return "YES" in result.content[0].text.strip().upper()

@app.route("/")
def index():
    return render_template("index.html", t=get_t())

@app.route("/set-language", methods=["POST"])
def set_language():
    session["language"] = request.form.get("language", "English")
    session.modified = True
    return redirect("/")

@app.route("/jobs-cached")
def jobs_cached():
    cv_data = get_cv_data()
    keywords = session.get("keywords", [])
    jobs = session.get("cached_jobs", [])
    location = session.get("cached_location", "")
    return render_template("jobs.html", jobs=jobs, keywords=keywords, location=location, cv=cv_data, t=get_t(), jobs_url="/jobs-cached")

@app.route("/upload-cv", methods=["POST"])
def upload_cv():
    if not check_limit("cv"):
        return render_template("index.html", error="You've reached today's limit. Come back tomorrow.", t=get_t())
    if "cv_file" not in request.files:
        return render_template("index.html", error="No file selected.", t=get_t())
    file = request.files["cv_file"]
    if file.filename == "":
        return render_template("index.html", error="No file selected.", t=get_t())
    if not allowed_file(file.filename):
        return render_template("index.html", error="Only PDF and DOCX files are supported.", t=get_t())
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    try:
        cv_text = extract_text_from_file(filepath)
        if not cv_text.strip():
            return render_template("index.html", error="Could not extract text from file.", t=get_t())
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        cv_check = client.messages.create(
            model=MODEL,
            max_tokens=10,
            messages=[{"role": "user", "content": f"Does this text look like a CV or resume? Reply only YES or NO.\n\n{cv_text[:500]}"}]
        )
        if "NO" in cv_check.content[0].text.strip().upper():
            return render_template("index.html", error="The uploaded file doesn't appear to be a CV or resume.", t=get_t())
        cv_data = parse_cv_with_claude(cv_text)
        increment_limit("cv")
        session["cv_name"] = cv_data.get("full_name", "")
        session["cv_email"] = cv_data.get("email", "")
        session["cv_skills"] = cv_data.get("skills", [])[:10]
        session["cv_experience"] = cv_data.get("experience_years", "")
        session["cv_summary"] = cv_data.get("summary", "")[:300]
        session["cv_education"] = cv_data.get("education", "")
        keywords = cv_data.get("keywords", [])
        session["keywords"] = keywords[:5]
        session["candidate_location"] = cv_data.get("location", "")
        session["jobs_url"] = "/jobs-cached"
        jobs = search_jobs(keywords, "")
        session["cached_jobs"] = jobs[:70]
        session["cached_location"] = ""
        session.modified = True
        return render_template("jobs.html", jobs=jobs[:70], keywords=keywords, location="", cv=get_cv_data(), t=get_t(), jobs_url="/jobs-cached")
    except Exception as e:
        return render_template("index.html", error=f"Error processing CV: {str(e)}", t=get_t())
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

@app.route("/search-jobs", methods=["GET", "POST"])
def search_jobs_route():
    cv_data = get_cv_data()
    keywords = session.get("keywords", [])
    if not keywords:
        return render_template("jobs.html", jobs=[], keywords=[], location="", cv={}, t=get_t(), jobs_url="/")
    if request.method == "POST":
        location = request.form.get("location", "")
    else:
        location = request.args.get("location", "")
    if not location and session.get("cached_jobs"):
        jobs = session["cached_jobs"]
    else:
        jobs = search_jobs(keywords, location)
        session["cached_jobs"] = jobs[:70]
        session["cached_location"] = location
        session.modified = True
    session["jobs_url"] = "/jobs-cached"
    return render_template("jobs.html", jobs=jobs, keywords=keywords, location=location, cv=cv_data, t=get_t(), jobs_url="/jobs-cached")

@app.route("/cover-letter", methods=["GET", "POST"])
def cover_letter():
    cv_data = get_cv_data()
    jobs_url = session.get("jobs_url", "/jobs-cached")
    job_title = request.args.get("job_title", "")
    company = request.args.get("company", "")
    if request.method == "POST":
        if not check_limit("cover"):
            return render_template("cover_letter.html", letter=None, job_title=job_title, company=company, cv=cv_data, t=get_t(), jobs_url=jobs_url, error="You've reached today's limit. Come back tomorrow.")
        job_title = request.form.get("job_title", "")
        company = request.form.get("company", "")
        job_description = request.form.get("job_description", "")
        language = session.get("language", "English")
        letter = generate_cover_letter(cv_data, job_title, company, job_description, language)
        letter = clean_text(letter)
        increment_limit("cover")
        session["last_letter"] = letter
        session["last_letter_job_title"] = job_title
        session["last_letter_company"] = company
        session.modified = True
        return redirect("/cover-letter-result")
    return render_template("cover_letter.html", letter=None, job_title=job_title, company=company, cv=cv_data, t=get_t(), jobs_url=jobs_url)

@app.route("/cover-letter-result", methods=["GET"])
def cover_letter_result():
    cv_data = get_cv_data()
    jobs_url = session.get("jobs_url", "/jobs-cached")
    return render_template("cover_letter.html",
        letter=session.get("last_letter", ""),
        job_title=session.get("last_letter_job_title", ""),
        company=session.get("last_letter_company", ""),
        cv=cv_data,
        t=get_t(),
        jobs_url=jobs_url
    )

@app.route("/answer", methods=["POST"])
def answer():
    if not check_limit("answer"):
        return render_template("index.html", error="You've reached today's limit. Come back tomorrow.", t=get_t())
    cv_data = get_cv_data()
    question = request.form.get("question", "")
    job_title = request.form.get("job_title", "")
    company = request.form.get("company", "")
    language = session.get("language", "English")
    answer_text = generate_application_answer(cv_data, question, job_title, company, language)
    answer_text = clean_text(answer_text)
    increment_limit("answer")
    session["last_answer"] = answer_text
    session["last_question"] = question
    session["last_job_title"] = job_title
    session["last_company"] = company
    session.modified = True
    return redirect("/answer-result")

@app.route("/answer-result", methods=["GET"])
def answer_result():
    jobs_url = session.get("jobs_url", "/jobs-cached")
    return render_template("answer.html",
        answer=session.get("last_answer", ""),
        question=session.get("last_question", ""),
        job_title=session.get("last_job_title", ""),
        company=session.get("last_company", ""),
        t=get_t(),
        jobs_url=jobs_url
    )

@app.route("/manual-search", methods=["GET"])
def manual_search():
    query = request.args.get("query", "").strip()
    location = request.args.get("location", "").strip()
    if not query:
        return render_template("index.html", error="Please enter a job title to search.", t=get_t())
    if len(query) < 2:
        return render_template("index.html", error="Please enter a more specific job title.", t=get_t())
    if not is_valid_job_title(query):
        return render_template("index.html", error=f"'{query}' doesn't look like a valid job title.", t=get_t())
    if location and not is_valid_location(location):
        return render_template("index.html", error=f"'{location}' doesn't seem to be a valid location.", t=get_t())
    jobs = search_jobs([query], location)
    session["cached_jobs"] = jobs[:70]
    session["cached_location"] = location
    session["jobs_url"] = "/jobs-cached"
    session.modified = True
    return render_template("jobs.html", jobs=jobs, keywords=[query], location=location, cv={}, t=get_t(), jobs_url="/jobs-cached")

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', debug=True)
