def generate_cover_letter(resume_text, job_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Ты HR. Напиши профессиональное сопроводительное письмо."
            },
            {
                "role": "user",
                "content": f"Резюме:\n{resume_text[:3000]}\n\nВакансия:\n{job_text[:3000]}"
            }
        ]
    )

    return response.choices[0].message.content