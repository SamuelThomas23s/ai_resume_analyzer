from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def ask_ai(system_prompt, user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_text[:4000]
            }
        ]
    )

    return response.choices[0].message.content


def analyze_resume(text):
    return ask_ai("""
Ты HR эксперт.

Дай:
1. Оценку резюме
2. Сильные стороны
3. Слабые стороны
4. Как улучшить
""", text)


def match_job(resume_text, job_text):
    return ask_ai("""
Сравни резюме с вакансией.

Дай:
1. % совпадения
2. Недостающие навыки
3. Советы
""", f"{resume_text}\n\n{job_text}")


def generate_cover_letter(resume_text, job_text):
    return ask_ai("""
Напиши профессиональное cover letter
""", f"{resume_text}\n\n{job_text}")


def ats_check(resume_text):
    return ask_ai("""
Оцени ATS совместимость резюме
""", resume_text)


def extract_data(resume_text):
    return ask_ai("""
Верни JSON:
- skills
- education
- experience
""", resume_text)


def keywords_suggestion(resume_text):
    return ask_ai("""
Дай ключевые слова для улучшения резюме
""", resume_text)


def skill_level_analysis(resume_text):
    return ask_ai("""
Определи уровень:
Junior / Middle / Senior
и объясни почему
""", resume_text)


# 🆕 NEW FEATURES

def interview_questions(resume_text):
    return ask_ai("""
Сгенерируй 10 вопросов для собеседования
по этому резюме
""", resume_text)


def salary_estimation(resume_text):
    return ask_ai("""
Оцени примерную зарплату кандидата
по навыкам и опыту.
Укажи диапазон.
""", resume_text)


def linkedin_optimization(resume_text):
    return ask_ai("""
Как улучшить LinkedIn профиль
на основе этого резюме?
""", resume_text)