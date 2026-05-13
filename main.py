from file_reader import read_file
from history import save_history

from ai import (
    smart_analysis,
    job_fit_score,
    cv_strength,
    interview_simulation
)

def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def menu():
    print("""
========== AI CAREER COACH V2 ==========

1 - Smart Analysis
2 - Job Fit Score
3 - CV Strength Score
4 - Interview Simulation

0 - Exit
========================================
""")


def main():
    print("🚀 AI CAREER COACH V2")

    while True:
        menu()

        choice = input("Выбор: ")

        if choice == "0":
            break

        resume_path = input("Путь к резюме: ")
        resume = read_file(resume_path)

        if not resume:
            print("Ошибка файла")
            continue

        result = ""

        if choice == "1":
            result = smart_analysis(resume)

        elif choice == "2":
            job = input("Вставь вакансию:\n")
            result = job_fit_score(resume, job)

        elif choice == "3":
            result = cv_strength(resume)

        elif choice == "4":
            result = interview_simulation(resume)

        else:
            print("Неверный выбор")
            continue

        print("\n========== RESULT ==========\n")
        print(result)

        save_result(result)
        save_history(f"Mode {choice}", result)

        print("\n✅ Сохранено")


if __name__ == "__main__":
    main()