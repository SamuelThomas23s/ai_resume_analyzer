from file_reader import read_file
from history import save_history

from ai import (
    analyze_resume,
    match_job,
    generate_cover_letter,
    ats_check,
    extract_data,
    keywords_suggestion,
    skill_level_analysis,
    interview_questions,
    salary_estimation,
    linkedin_optimization
)

def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def print_menu():
    print("""
========= AI Resume Analyzer PRO =========

1 - Анализ резюме
2 - Сравнение с вакансией
3 - Cover Letter
4 - ATS проверка
5 - JSON структура
6 - Ключевые слова
7 - Уровень кандидата
8 - Interview Questions
9 - Salary Estimation
10 - LinkedIn Optimization

0 - Выход

==========================================
""")


def main():
    print("🚀 AI Resume Analyzer PRO MAX")

    while True:
        print_menu()

        choice = input("Выбор: ")

        if choice == "0":
            print("Пока!")
            break

        resume_path = input("Путь к резюме: ")

        resume_text = read_file(resume_path)

        if not resume_text:
            print("Ошибка чтения файла")
            continue

        result = ""

        if choice == "1":
            result = analyze_resume(resume_text)

        elif choice == "2":
            job_text = input("Вставь описание вакансии:\n")
            result = match_job(resume_text, job_text)

        elif choice == "3":
            job_text = input("Вставь описание вакансии:\n")
            result = generate_cover_letter(resume_text, job_text)

        elif choice == "4":
            result = ats_check(resume_text)

        elif choice == "5":
            result = extract_data(resume_text)

        elif choice == "6":
            result = keywords_suggestion(resume_text)

        elif choice == "7":
            result = skill_level_analysis(resume_text)

        elif choice == "8":
            result = interview_questions(resume_text)

        elif choice == "9":
            result = salary_estimation(resume_text)

        elif choice == "10":
            result = linkedin_optimization(resume_text)

        else:
            print("Неверный выбор")
            continue

        print("\n========== RESULT ==========\n")
        print(result)

        save_result(result)

        save_history(f"Mode {choice}", result)

        print("\n✅ Сохранено в result.txt")
        print("✅ История сохранена")


if __name__ == "__main__":
    main()