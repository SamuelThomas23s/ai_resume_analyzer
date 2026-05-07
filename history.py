from datetime import datetime

HISTORY_FILE = "analysis_history.txt"

def save_history(title, content):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"{datetime.now()}\n")
        f.write(f"{title}\n\n")
        f.write(content)
        f.write("\n")