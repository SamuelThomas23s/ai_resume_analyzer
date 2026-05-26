from database import get_all_candidates


def analyze_scores():
    candidates = get_all_candidates()

    scores = []

    for c in candidates:
        try:
            score = int(''.join(filter(str.isdigit, c[2])))
            scores.append(score)
        except:
            pass

    if not scores:
        return "No data"

    return {
        "total": len(scores),
        "average": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    }