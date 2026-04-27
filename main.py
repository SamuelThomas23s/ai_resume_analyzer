from file_reader import read_file
from ai import analyze_resume

def main():
    print("AI Resume Analyzer 🚀")

    path = input("Введи путь к резюме (txt/pdf): ")

    text = read_file(path)

    if not text:
        print("Ошибка чтения файла")
        return

    print("Анализирую...\n")

    result = analyze_resume(text)

    print("\n=== РЕЗУЛЬТАТ ===\n")
    print(result)


if __name__ == "__main__":
    main()