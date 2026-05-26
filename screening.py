from database import get_all_candidates


def auto_screen(min_score=70):
    candidates = get_all_candidates()

    passed = []
    rejected = []

    for c in candidates:
        try:
            score = int(''.join(filter(str.isdigit, c[2])))

            if score >= min_score:
                passed.append(c)
            else:
                rejected.append(c)

        except:
            rejected.append(c)

    return {
        "passed": passed,
        "rejected": rejected
    }