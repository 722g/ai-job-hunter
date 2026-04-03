import PyPDF2
import docx
import anthropic
import json
from config import ANTHROPIC_API_KEY, MODEL

def extract_text_from_file(filepath):
    if filepath.endswith(".pdf"):
        text = ""
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    elif filepath.endswith(".docx"):
        doc = docx.Document(filepath)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def parse_cv_with_claude(cv_text):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    prompt = "Analyze this CV and return ONLY a valid JSON object with these exact keys: full_name, email, phone, location, summary, skills (array), job_titles (array), experience_years (number), education (string), languages (array), keywords (array of 10 job search keywords). CV TEXT: " + cv_text
    message = client.messages.create(model=MODEL, max_tokens=1500, messages=[{"role": "user", "content": prompt}])
    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())
