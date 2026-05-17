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


# 📊 SMART ANALYSIS
def smart_analysis(resume):
    return ask_ai("""
Ты HR эксперт.

Сделай:
- анализ
- ошибки
- рекомендации
""", resume)


# 🆚 COMPARE CANDIDATES (НОВОЕ)
def compare_candidates(resume1, resume2, job):
    return ask_ai("""
Сравни двух кандидатов под вакансию.

Верни:
- кто лучше
- почему
- сильные/слабые стороны
""", f"JOB:\n{job}\n\nCANDIDATE 1:\n{resume1}\n\nCANDIDATE 2:\n{resume2}")


# 🧠 HIRING DECISION (НОВОЕ)
def hiring_decision(resume, job):
    return ask_ai("""
Ты HR директор.

Ответь:
- нанять или нет
- почему
- риски
- потенциал роста
""", f"{job}\n\n{resume}")


# ⚠️ RISK DETECTOR (НОВОЕ)
def career_risk_detector(resume):
    return ask_ai("""
Оцени карьерные риски:

- нестабильность навыков
- пробелы
- слабые зоны
- риски найма
""", resume)


# 📊 EXISTING WRAPPERS
def job_fit_score(resume, job):
    return ask_ai("Match score 0-100%", f"{resume}\n\n{job}")


def cv_strength(resume):
    return ask_ai("CV score 0-10", resume)


def interview_simulation(resume):
    return ask_ai("Mock interview", resume)


def skill_gap_analysis(resume, job):
    return ask_ai("Skill gaps", f"{resume}\n\n{job}")


def career_recommendations(resume):
    return ask_ai("Career recommendations", resume)


def resume_dashboard(resume):
    return ask_ai("Dashboard score", resume)


def generate_summary(resume):
    return ask_ai("Summary + LinkedIn bio", resume)