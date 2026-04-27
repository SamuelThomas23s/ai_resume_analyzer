from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def analyze_resume(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
Ты HR эксперт.

Проанализируй резюме и дай:
1. Оценку (1-10)
2. Сильные стороны
3. Слабые стороны
4. Как улучшить
5. Переписанную улучшенную версию
"""
            },
            {"role": "user", "content": text[:4000]}
        ]
    )

    return response.choices[0].message.content