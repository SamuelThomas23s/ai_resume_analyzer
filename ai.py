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


# 🧠 SMART ANALYSIS
def smart_analysis(resume):
    return ask_ai("""
Ты AI HR эксперт.

Сделай:
1. Анализ резюме
2. Ошибки
3. Что улучшить
4. Рекомендации
""", resume)


# 🎯 JOB FIT SCORE
def job_fit_score(resume, job):
    return ask_ai("""
Сравни резюме и вакансию.

Верни:
- Match Score %
- Missing Skills
- Recommendations
""", f"{resume}\n\n{job}")


# 📈 CV STRENGTH
def cv_strength(resume):
    return ask_ai("""
Оцени:
- structure
- skills
- experience
- ATS readiness

Дай итоговый score 0-10
""", resume)


# 🎤 INTERVIEW
def interview_simulation(resume):
    return ask_ai("""
Проведи mock interview:
- 5 вопросов
- оценка кандидата
- feedback
""", resume)


# 🆕 SKILL GAP ANALYSIS
def skill_gap_analysis(resume, job):
    return ask_ai("""
Сравни навыки кандидата и вакансии.

Верни:
1. Missing skills
2. Priority skills
3. Что изучать первым
4. Насколько кандидат подходит
""", f"{resume}\n\n{job}")


# 🆕 CAREER RECOMMENDATIONS
def career_recommendations(resume):
    return ask_ai("""
На основе резюме:

1. Лучшие карьерные направления
2. Подходящие профессии
3. Что изучать дальше
4. Как увеличить зарплату
""", resume)


# 🆕 RESUME DASHBOARD
def resume_dashboard(resume):
    return ask_ai("""
Создай dashboard оценки резюме:

- Skills Score
- Experience Score
- ATS Score
- Readability
- Final Score

Используй понятный формат.
""", resume)


# 🆕 SUMMARY GENERATOR
def generate_summary(resume):
    return ask_ai("""
Создай:

1. Professional Summary
2. About Me
3. LinkedIn Bio

на основе резюме.
""", resume)