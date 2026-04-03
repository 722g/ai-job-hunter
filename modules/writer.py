import anthropic
from config import ANTHROPIC_API_KEY, MODEL

def generate_cover_letter(cv_data, job_title, company, job_description, language="English"):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""Write a professional cover letter for this candidate applying to this job.

CANDIDATE PROFILE:
Name: {cv_data.get('full_name', 'The Candidate')}
Email: {cv_data.get('email', '')}
Phone: {cv_data.get('phone', '')}
Location: {cv_data.get('location', '')}
Skills: {', '.join(cv_data.get('skills', []))}
Experience: {cv_data.get('experience_years', 'N/A')} years
Summary: {cv_data.get('summary', '')}
Education: {cv_data.get('education', '')}

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
6. At the top include candidate name, their EXACT email ({cv_data.get('email', '')}), and phone number

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

    prompt = f"""Answer this job application question for this candidate.

CANDIDATE PROFILE:
Name: {cv_data.get('full_name', 'The Candidate')}
Skills: {', '.join(cv_data.get('skills', []))}
Experience: {cv_data.get('experience_years', 'N/A')} years
Summary: {cv_data.get('summary', '')}

JOB: {job_title} at {company}

APPLICATION QUESTION: {question}

Write a strong, specific answer that:
1. Directly addresses the question
2. Uses examples from the candidate's background
3. Is 2-3 paragraphs
4. Sounds natural and confident

Write the ENTIRE answer in {language} language only.
Write ONLY the answer, no extra explanation."""

    message = client.messages.create(
        model=MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()