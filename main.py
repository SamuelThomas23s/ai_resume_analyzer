from file_reader import read_file
from history import save_history

from ai import (
    smart_analysis,
    compare_candidates,
    hiring_decision,
    career_risk_detector
)


def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def menu():
    print("""
========== AI HR SYSTEM V4 ==========

1 - Smart Analysis
2 - Compare Candidates
3 - Hiring Decision
4 - Career Risk Detector

0 - Exit
=====================================
""")


def main():
    print("🚀 AI HR SYSTEM V4")

    while True:
        menu()

        choice = input("Выбор: ")

        if choice == "0":
            break

        if choice == "1":
            path = input("Резюме:\n")
            resume = read_file(path)

            result = smart_analysis(resume)

        elif choice == "2":
            job = input("Вакансия:\n")

            r1 = read_file(input("Candidate 1:\n"))
            r2 = read_file(input("Candidate 2:\n"))

            result = compare_candidates(r1, r2, job)

        elif choice == "3":
            job = input("Вакансия:\n")
            resume = read_file(input("Resume:\n"))

            result = hiring_decision(resume, job)

        elif choice == "4":
            resume = read_file(input("Resume:\n"))
            result = career_risk_detector(resume)

        else:
            print("Неверный выбор")
            continue

        print("\n========== RESULT ==========\n")
        print(result)

        save_result(result)
        save_history(f"Mode {choice}", result)

        print("\n✅ Saved")


if __name__ == "__main__":
    main()