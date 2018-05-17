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
    return score

def scoreNeighboursModifier(mel):
    score = 0
    length = len(mel)
    n = 0
    for i in range(length - 1):
        check = mel[i] - mel[i + 1]

        if abs(check) == 1:
            n += 1
        else:
            score += n*n
            n = 0
    return score
