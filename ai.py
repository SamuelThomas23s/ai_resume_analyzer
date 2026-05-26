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


# 🤖 AUTO SCREENING DECISION
def screening_decision(resume):
    return ask_ai("""
Ты HR AI.

Реши:
- pass / reject
- причина
- уровень кандидата
""", resume)


# 📩 AUTO INVITE GENERATOR
def auto_invite(resume, job):
    return ask_ai("""
Сгенерируй приглашение на интервью.

Коротко, профессионально.
""", f"{resume}\n\n{job}")