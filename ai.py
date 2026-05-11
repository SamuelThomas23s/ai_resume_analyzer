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


# 📊 Анализ резюме
def analyze_resume(text):
    return ask_ai("""
Ты HR эксперт.

Проанализируй резюме:
1. Оценка
2. Сильные стороны
3. Слабые стороны
4. Как улучшить
""", text)


# 🎯 Match с вакансией
def match_job(resume_text, job_text):
    return ask_ai("""
Сравни резюме с вакансией.

Дай:
1. % совпадения
2. Недостающие навыки
3. Советы
""", f"{resume_text}\n\n{job_text}")


# ✍️ Cover Letter
def generate_cover_letter(resume_text, job_text):
    return ask_ai("""
Напиши профессиональное cover letter
""", f"{resume_text}\n\n{job_text}")


# 🤖 ATS
def ats_check(resume_text):
    return ask_ai("""
Оцени ATS совместимость резюме
""", resume_text)


# 📄 JSON структура
def extract_data(resume_text):
    return ask_ai("""
Верни JSON:
- skills
- education
- experience
""", resume_text)


# 🔑 Keywords
def keywords_suggestion(resume_text):
    return ask_ai("""
Дай ключевые слова для улучшения резюме
""", resume_text)


# 🧠 Skill level
def skill_level_analysis(resume_text):
    return ask_ai("""
Определи уровень:
Junior / Middle / Senior
и объясни почему
""", resume_text)


# ❓ Interview Questions
def interview_questions(resume_text):
    return ask_ai("""
Сгенерируй 10 вопросов для собеседования
""", resume_text)


# 💰 Salary
def salary_estimation(resume_text):
    return ask_ai("""
Оцени зарплату кандидата
и укажи диапазон
""", resume_text)


# 🌐 LinkedIn
def linkedin_optimization(resume_text):
    return ask_ai("""
Как улучшить LinkedIn профиль?
""", resume_text)


# 🚀 Career Roadmap
def career_roadmap(resume_text):
    return ask_ai("""
Создай roadmap:

1. Текущий уровень
2. Что учить
3. План на 6 месяцев
4. План на 1 год
""", resume_text)


# ✍️ Rewrite Resume
def rewrite_resume(resume_text):
    return ask_ai("""
Полностью перепиши резюме
в современном профессиональном стиле
""", resume_text)


# ⚠️ Weakness Detector
def weakness_detector(resume_text):
    return ask_ai("""
Найди:
- слабые навыки
- пробелы
- missing skills
- что мешает росту
""", resume_text)


# 🌍 Translate Resume
def translate_resume(resume_text, language):
    return ask_ai(f"""
Переведи резюме на язык: {language}

Сохрани профессиональный стиль.
""", resume_text)