from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def generate_email(candidate_name, job, status):
    prompt = f"""
Ты HR ассистент.

Напиши email кандидату.

Имя: {candidate_name}
Вакансия: {job}
Статус: {status} (invite / reject / offer)

Стиль: профессиональный, короткий.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Ты HR email assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content