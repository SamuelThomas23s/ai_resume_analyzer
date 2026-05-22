from file_reader import read_file

from hr_logs import init_logs, save_decision, get_logs
from email_generator import generate_email

from ai import interview_report, top_candidate_alert


def main():
    init_logs()

    print("🚀 AI HR SYSTEM V7")

    while True:
        print("""
========== HR CONTROL CENTER ==========

1 - Generate Email
2 - Save Hiring Decision
3 - View Logs
4 - Interview Report
5 - Top Candidate Alert

0 - Exit
=======================================
""")

        choice = input("Choice: ")

        # 📧 EMAIL GENERATION
        if choice == "1":
            name = input("Candidate name: ")
            job = input("Job: ")
            status = input("Status (invite/reject/offer): ")

            email = generate_email(name, job, status)

            print("\n📧 EMAIL:\n")
            print(email)

        # 🧾 SAVE DECISION
        elif choice == "2":
            candidate = input("Candidate: ")
            job = input("Job: ")
            decision = input("Decision: ")
            reason = input("Reason: ")

            save_decision(candidate, job, decision, reason)

            print("Saved ✔")

        # 📜 LOGS
        elif choice == "3":
            logs = get_logs()

            print("\n📊 HR LOGS:")
            for l in logs:
                print(l)

        # 🧠 INTERVIEW REPORT
        elif choice == "4":
            text = input("Paste interview notes:\n")
            result = interview_report(text)

            print("\n========== REPORT ==========\n")
            print(result)

        # 🔔 TOP ALERT
        elif choice == "5":
            text = input("Candidate info:\n")
            result = top_candidate_alert(text)

            print("\n🚨 ALERT:\n")
            print(result)

        elif choice == "0":
            break

        else:
            print("Invalid")


if __name__ == "__main__":
    main()