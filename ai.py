from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def analyze_resume(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
Ты HR эксперт.

Дай:
1. Оценку (1-10)
2. Сильные стороны
3. Слабые стороны
4. Как улучшить
"""},
            {"role": "user", "content": text[:4000]}
        ]
    )
    return response.choices[0].message.content


def match_job(resume_text, job_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
Сравни резюме с вакансией:
1. % совпадения
2. Чего не хватает
3. Как улучшить
"""},
            {"role": "user", "content": f"{resume_text[:3000]}\n\n{job_text[:3000]}"}
        ]
    )
    return response.choices[0].message.content


def generate_cover_letter(resume_text, job_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Напиши сопроводительное письмо"},
            {"role": "user", "content": f"{resume_text[:3000]}\n\n{job_text[:3000]}"}
        ]
    )
    return response.choices[0].message.content


def ats_check(resume_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Оцени ATS: пройдет или нет + почему"},
            {"role": "user", "content": resume_text[:4000]}
        ]
    )
    return response.choices[0].message.content


def extract_data(resume_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Вытащи JSON: навыки, опыт, образование"},
            {"role": "user", "content": resume_text[:4000]}
        ]
    )
    return response.choices[0].message.content


def keywords_suggestion(resume_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Дай ключевые слова для резюме"},
            {"role": "user", "content": resume_text[:4000]}
        ]
    )
    return response.choices[0].message.content


def skill_level_analysis(resume_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Определи уровень: Junior/Middle/Senior + почему"},
            {"role": "user", "content": resume_text[:4000]}
        ]
    )
    return response.choices[0].message.content