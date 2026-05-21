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


# 🧠 TALENT MATCH (НОВОЕ)
def talent_match(job, candidates_text):
    return ask_ai("""
Ты HR AI.

Найди лучших кандидатов под вакансию.

Верни:
- TOP кандидатов
- почему они подходят
- ranking
""", f"JOB:\n{job}\n\nCANDIDATES:\n{candidates_text}")


# ⚡ HIRING RECOMMENDATION
def hiring_recommendation(candidates_text):
    return ask_ai("""
Ты HR директор.

Скажи:
- кого нанять
- почему
- риски
- топ 1 кандидат
""", candidates_text)