def scoreNeighbours(mel):
    score = 0
    length = len(mel)
    for i in range(1, length - 1):
        checkLeft = mel[i] - mel[i - 1]
        checkRight = mel[i] - mel[i + 1]
        if abs(checkLeft) == 1:
            score += 1
        if abs(checkRight) == 1:
            score += 1
