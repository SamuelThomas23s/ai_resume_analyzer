import os
from file_reader import read_file
from database import init_db, save_candidate, search_candidates
from report import generate_pdf_report
from ai import batch_analysis, extract_score, smart_search


def scan_folder(folder):
    files = os.listdir(folder)
    return [os.path.join(folder, f) for f in files if f.endswith(".pdf") or f.endswith(".txt")]


def main():
    init_db()

    print("🚀 AI HR SYSTEM V5")

    while True:
        print("""
1 - Batch Analysis (folder)
2 - Save Candidate
3 - Search Candidates
4 - Generate PDF Report
0 - Exit
""")

        choice = input("Choice: ")

        if choice == "0":
            break

        # 📊 BATCH ANALYSIS
        if choice == "1":
            folder = input("Folder path: ")
            files = scan_folder(folder)

            all_text = ""

            for f in files:
                text = read_file(f)
                all_text += f"\n\nFILE: {f}\n{text}"

            result = batch_analysis(all_text)

            print(result)

            generate_pdf_report("report.pdf", result)

        # 💾 SAVE CANDIDATE
        elif choice == "2":
            name = input("Candidate name: ")
            resume = read_file(input("Resume path: "))
            score = extract_score(resume)

            save_candidate(name, score)

            print("Saved to DB")

        # 🔍 SEARCH
        elif choice == "3":
            keyword = input("Search: ")
            results = search_candidates(keyword)

            print(results)

        # 📄 PDF REPORT
        elif choice == "4":
            text = input("Paste analysis text: ")
            generate_pdf_report("hr_report.pdf", text)

            print("PDF created")

        else:
            print("Invalid")


if __name__ == "__main__":
    main()