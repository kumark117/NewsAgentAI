def growth_score(history):

    if len(history) < 2:
        return 0

    return history[-1] - history[-2]