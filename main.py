from file_reader import read_file

from database import (
    init_db,
    get_all_candidates,
    get_candidates_count,
    get_best_candidates
)

from ai import (
    talent_match,
    hiring_recommendation
)


def main():
    init_db()

    print("🚀 AI HR SYSTEM V6")

    while True:
        print("""
========== DASHBOARD ==========

1 - Show Stats
2 - Show Best Candidates
3 - Talent Match (Job → DB)
4 - Hiring Recommendation

0 - Exit
===============================
""")

        choice = input("Choice: ")

        # 📊 STATS DASHBOARD
        if choice == "1":
            count = get_candidates_count()
            best = get_best_candidates(3)

            print("\n📊 SYSTEM STATS")
            print(f"Total candidates: {count}")
            print("Top 3:")

            for b in best:
                print(b)

        # 🏆 BEST CANDIDATES
        elif choice == "2":
            best = get_best_candidates(5)

            print("\n🏆 TOP CANDIDATES:")
            for c in best:
                print(c)

        # 🎯 TALENT MATCH
        elif choice == "3":
            job = input("Paste job description:\n")
            candidates = get_all_candidates()

            text = "\n".join([str(c) for c in candidates])

            result = talent_match(job, text)

            print("\n========== RESULT ==========\n")
            print(result)

        # ⚡ HIRING DECISION
        elif choice == "4":
            candidates = get_all_candidates()
            text = "\n".join([str(c) for c in candidates])

            result = hiring_recommendation(text)

            print("\n========== RESULT ==========\n")
            print(result)

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()