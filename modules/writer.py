import anthropic
from config import ANTHROPIC_API_KEY, MODEL

def generate_cover_letter(cv_data, job_title, company, job_description, language="English"):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    name = cv_data.get('full_name', '') or 'The Candidate'
    email = cv_data.get('email', '') or ''
    skills = cv_data.get('skills', []) or []
    experience = cv_data.get('experience_years', '') or 'several'
    summary = cv_data.get('summary', '') or ''
    education = cv_data.get('education', '') or ''

    prompt = f"""Write a professional cover letter for this candidate applying to this job.

CANDIDATE PROFILE:
Name: {name}
Email: {email}
Skills: {', '.join(skills) if skills else 'various technical skills'}
Experience: {experience} years
Summary: {summary}
Education: {education}

JOB DETAILS:
Title: {job_title}
Company: {company}
Description: {job_description}

Write a compelling, personalized cover letter that:
1. Opens with a strong hook
2. Matches candidate skills to job requirements
3. Shows enthusiasm for the company
4. Is professional but not generic
5. Is 3-4 paragraphs long
6. At the top include only the candidate name and email if available

IMPORTANT: Write in plain text only. NO markdown formatting. NO asterisks. NO hashtags. NO dashes as separators. NO bold text. Just clean plain text paragraphs.

Write the ENTIRE cover letter in {language} language only.
Write ONLY the cover letter, no extra explanation."""

    message = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()


def generate_application_answer(cv_data, question, job_title, company, language="English"):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    name = cv_data.get('full_name', '') or 'The Candidate'
    skills = cv_data.get('skills', []) or []
    experience = cv_data.get('experience_years', '') or 'several'
    summary = cv_data.get('summary', '') or ''

    prompt = f"""Answer this job application question for this candidate.

CANDIDATE PROFILE:
Name: {name}
Skills: {', '.join(skills) if skills else 'various technical skills'}
Experience: {experience} years
Summary: {summary}

JOB: {job_title} at {company}

APPLICATION QUESTION: {question}

Write a strong, specific answer that:
1. Directly addresses the question
2. Uses examples from the candidate's background
3. Is 2-3 paragraphs
4. Sounds natural and confident

IMPORTANT: Write in plain text only. NO markdown formatting. NO asterisks. NO hashtags. NO bold text. Just clean plain text paragraphs.

Write the ENTIRE answer in {language} language only.
Write ONLY the answer, no extra explanation."""

    message = client.messages.create(
        model=MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()
