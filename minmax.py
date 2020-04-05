import math


def minmax(value, turn, sumPoints=0):
    if sumPoints > 21:
        if turn:
            return 1
        else:
            return -1
    elif sumPoints == 21:
        return 0
    if turn:
        maxEval = -math.inf
        for item in value:
            evalX = minmax(value, False, sumPoints + item)
            maxEval = max(maxEval, evalX)
        return maxEval
    else:
        minEval = math.inf
        for item in value:
            evalY = minmax(value, True, sumPoints + item)
            minEval = min(minEval, evalY)
        return minEval


def whowin(score):
    if score == 0:
        return "DRAW"
    elif score == 1:
        return "PROT WIN"
    else:
        return "ANT WIN"


values = [4, 5, 6]
result = whowin(minmax(values, True))
print(result)
