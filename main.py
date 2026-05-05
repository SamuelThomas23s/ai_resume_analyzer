from file_reader import read_file
from ai import analyze_resume, match_job, generate_cover_letter

def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)

def main():
    print("AI Resume Analyzer PRO 🚀")

    resume_path = input("Путь к резюме: ")
    resume_text = read_file(resume_path)

    if not resume_text:
        print("Ошибка чтения резюме")
        return

    print("""
Выбери режим:
1 - Анализ резюме
2 - Сравнение с вакансией
3 - Cover Letter
""")

    choice = input("Выбор: ")

    if choice == "1":
        result = analyze_resume(resume_text)

    elif choice == "2":
        job_text = input("Вставь описание вакансии:\n")
        result = match_job(resume_text, job_text)

    elif choice == "3":
        job_text = input("Вставь описание вакансии:\n")
        result = generate_cover_letter(resume_text, job_text)

    else:
        print("Неверный выбор")
        return

    print("\n=== РЕЗУЛЬТАТ ===\n")
    print(result)

    save_result(result)
    print("\nСохранено в result.txt")

if __name__ == "__main__":
    main()