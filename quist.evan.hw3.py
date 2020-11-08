import WarriorFlip


def nWarriors(n, p):
    num = 0
    for i in range(n):
        num += WarriorFlip.WarriorFlip(p)
    return n - num


def HundyWarriors():
    for i in range(1, 100, 1):
        print(i / 100, "-", nWarriors(100, i / 100))


def Warriors32(n):
    return nWarriors(n, .32)


def Optimum32():
    for i in range(7):
        num = 0
        wins = 0
        for x in range(100000):
            temp = Warriors32(i)
            num += temp
            if temp == 1:
                wins += 1
        print("Number of wins:", wins)
        print("Win percentage:", wins/100000)
        num /= 100000
        print(i, " - ", num)
        # It appears that 3 is about the point of highest success.

