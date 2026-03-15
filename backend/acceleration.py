def acceleration_score(history):

    if len(history) < 3:
        return 0

    g1 = history[-2] - history[-3]
    g2 = history[-1] - history[-2]

    return g2 - g1