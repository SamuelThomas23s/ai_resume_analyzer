from screening import auto_screen
from analytics import analyze_scores
from ai import screening_decision


def main():
    print("🚀 AI HR SYSTEM V8")

    while True:
        print("""
========== AI HR PLATFORM V8 ==========

1 - Web Dashboard (run Flask)
2 - Analytics
3 - Auto Screening

0 - Exit
=======================================
""")

        choice = input("Choice: ")

        # 🌐 WEB DASHBOARD
        if choice == "1":
            from web_app import app
            app.run(debug=True)

        # 📊 ANALYTICS
        elif choice == "2":
            print(analyze_scores())

        # 🤖 AUTO SCREENING
        elif choice == "3":
            from database import get_all_candidates

            candidates = get_all_candidates()

            for c in candidates:
                result = screening_decision(str(c))
                print("\n---")
                print(c)
                print(result)

        elif choice == "0":
            break

        else:
            print("Invalid")


if __name__ == "__main__":
    main()