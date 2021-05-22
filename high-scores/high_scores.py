def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    # scores.sort(reverse=True)
    #1 return [scores[i] for i in range(3) if i < len(scores)]
    #2 return scores[:3]
    return sorted(scores, reverse=True)[:3]

# exercism submit Exercism/python/high-scores/high_scores.py