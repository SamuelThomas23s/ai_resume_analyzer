from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def ask_ai(system, user):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user[:4000]}
        ]
    ).choices[0].message.content


# 🧠 AI INTERVIEW REPORT (НОВОЕ)
def interview_report(interview_text):
    return ask_ai("""
Ты HR директор.

Сделай итог интервью:
- оценка кандидата
- сильные стороны
- слабые стороны
- hire / no hire
- причины
""", interview_text)


# 🔔 TOP ALERT SYSTEM
def top_candidate_alert(candidate_text):
    return ask_ai("""
Определи:

- является ли кандидат ТОП
- стоит ли срочно нанять
- риск упустить кандидата
""", candidate_text)