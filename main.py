from file_reader import read_file
from ai import (
    analyze_resume,
    match_job,
    generate_cover_letter,
    ats_check,
    extract_data,
    keywords_suggestion,
    skill_level_analysis
)

def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def main():
    print("AI Resume Analyzer PRO 🚀")

    resume_path = input("Путь к резюме: ")
    resume_text = read_file(resume_path)

    if not resume_text:
        print("Ошибка чтения файла")
        return

    print("""
Выбери режим:
1 - Анализ резюме
2 - Сравнение с вакансией
3 - Cover Letter
4 - ATS проверка
5 - JSON структура
6 - Ключевые слова
7 - Уровень кандидата
""")

    choice = input("Выбор: ")

    if choice == "1":
        result = analyze_resume(resume_text)

    elif choice == "2":
        job_text = input("Вставь вакансию:\n")
        result = match_job(resume_text, job_text)

    elif choice == "3":
        job_text = input("Вставь вакансию:\n")
        result = generate_cover_letter(resume_text, job_text)

    elif choice == "4":
        result = ats_check(resume_text)

    elif choice == "5":
        result = extract_data(resume_text)

    elif choice == "6":
        result = keywords_suggestion(resume_text)

    elif choice == "7":
        result = skill_level_analysis(resume_text)

    else:
        print("Неверный выбор")
        return

    print("\n=== РЕЗУЛЬТАТ ===\n")
    print(result)

    save_result(result)
    print("\nСохранено в result.txt")


if __name__ == "__main__":
    main()