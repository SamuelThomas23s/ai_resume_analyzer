from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def ask_ai(system, user):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user[:4000]}
        ]
    )
    return response.choices[0].message.content


# 📊 SMART ANALYSIS (НОВОЕ)
def smart_analysis(resume):
    return ask_ai("""
Ты AI карьерный эксперт.

Сделай:
1. Анализ резюме
2. Проблемы
3. Рекомендации
4. Что улучшить прямо сейчас
""", resume)


# 🎯 AUTO JOB FIT SCORE (НОВОЕ)
def job_fit_score(resume, job):
    return ask_ai("""
Оцени совпадение резюме и вакансии.

Верни:
- Score 0–100%
- Почему
- Чего не хватает
""", f"{resume}\n\n{job}")


# 📈 CV STRENGTH SCORE (НОВОЕ)
def cv_strength(resume):
    return ask_ai("""
Оцени резюме:

1. Структура
2. Навыки
3. Опыт
4. Сильные стороны

Дай итоговый score 0–10
""", resume)


# 🧠 INTERVIEW SIMULATION (НОВОЕ)
def interview_simulation(resume):
    return ask_ai("""
Ты интервьюер.

Проведи собеседование:
- задай 5 вопросов
- после ответов оцени кандидата
- дай фидбек
""", resume)


# ✍️ EXISTING FUNCTIONS (упрощённые)

def analyze_resume(text):
    return ask_ai("HR эксперт: анализ резюме", text)


def match_job(resume, job):
    return job_fit_score(resume, job)


def generate_cover_letter(resume, job):
    return ask_ai("Напиши cover letter", f"{resume}\n\n{job}")


def ats_check(resume):
    return ask_ai("ATS проверка", resume)


def extract_data(resume):
    return ask_ai("JSON структура резюме", resume)


def keywords_suggestion(resume):
    return ask_ai("Ключевые слова для резюме", resume)


def skill_level_analysis(resume):
    return ask_ai("Junior/Middle/Senior определение", resume)


def interview_questions(resume):
    return ask_ai("Сгенерируй 10 вопросов", resume)


def salary_estimation(resume):
    return ask_ai("Оцени зарплату", resume)


def linkedin_optimization(resume):
    return ask_ai("LinkedIn улучшение", resume)


def career_roadmap(resume):
    return ask_ai("Карьерный план", resume)


def rewrite_resume(resume):
    return ask_ai("Перепиши резюме лучше", resume)


def weakness_detector(resume):
    return ask_ai("Найди слабые места", resume)


def translate_resume(resume, lang):
    return ask_ai(f"Переведи на {lang}", resume)