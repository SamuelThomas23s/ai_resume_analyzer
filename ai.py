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


def batch_analysis(resumes_text):
    return ask_ai("""
Проанализируй список резюме.

Дай:
- рейтинг каждого
- кто лучший
- почему
""", resumes_text)


def extract_score(resume):
    return ask_ai("""
Дай только числовой score 0-100
""", resume)


def smart_search(query, database_text):
    return ask_ai("""
Найди лучших кандидатов по запросу:
""", f"{query}\n\n{database_text}")