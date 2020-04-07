import math, copy


class Field:

    def __init__(self, value, depth, child, item):
        self.item = item
        self.depth = depth
        self.child = child
        self.value = value

    def __str__(self):
        return "Depth:" + str(self.depth) + " Value choose: " + str(self.item) + " Wins:" + str(self.value)


def minmax(values, turn, temp, sumPoints=0, depth=0, item=0):
    if sumPoints > 21:
        if turn:
            temp.append(Field(sumPoints-21, depth, sumPoints, item))
            return sumPoints - 21
        else:
            temp.append(Field(21 - sumPoints, depth, sumPoints, item))
            return 21 - sumPoints
    elif sumPoints == 21:
        temp.append(Field(0, depth, sumPoints, item))
        return 0
    else:
        temp.append(Field(0, depth, temp[-1], item))
    if turn:
        maxEval = -math.inf
        for item in values:
            evalX = minmax(values, False, temp, sumPoints + item, depth + 1, item)
            maxEval = max(evalX, maxEval)
        help = None
        for i in range(1, 4):
            if temp[-i].value == maxEval:
                help = temp[-i]
        temp.pop(-1)
        temp.pop(-1)
        temp.pop(-1)
        temp[-1].child = help
        temp[-1].value = help.value
        return maxEval
    else:
        minEval = math.inf
        for item in values:
            evalY = minmax(values, True, temp, sumPoints + item, depth + 1, item)
            minEval = min(evalY, minEval)
        help = None
        for i in range(1, 4):
            if temp[-i].value == minEval:
                help = temp[-i]
        temp.pop(-1)
        temp.pop(-1)
        temp.pop(-1)
        temp[-1].child = help
        temp[-1].value = help.value
        return minEval



wartosci = [4, 5, 6]
tab = [Field(0, 0, None, 0)]
zmienna = minmax(wartosci, True, tab)
printer = tab[1]
print("Negative score: Antagonist wins, Positive score: Protagonist wins, Zero: Draw")
while isinstance(printer, int) is False:
    print(printer)
    printer = printer.child
