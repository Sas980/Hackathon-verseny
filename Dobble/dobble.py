import random
import sys


def first_row(n, symbols):
    deck1 = [random.choice(symbols)]
    repeat = True
    while repeat:
        if len(deck1) <= n - 1:
            x = random.choice(symbols)
            if x not in deck1:
                deck1.append(x)
        else:
            repeat = False
    return deck1


def second_row(n, deck1):
    deck2 = [random.choice(deck1)]
    repeat = True
    while repeat:
        if len(deck2) <= n - 1:
            x = random.choice(deck1)
            if x not in deck2:
                deck2.append(x)
        else:
            repeat = False
    return deck2


def game(deck1, deck2):
    deck1.clear()
    deck1.append(random.choice(deck2))
    repeat = True
    while repeat:
        if len(deck1) <= n - 1:
            x = random.choice(symbols)
            if x not in deck1:
                deck1.append(x)
        else:
            repeat = False
    return deck1


def game2(deck1, deck2):
    deck2.clear()
    deck2.append(random.choice(deck1))
    repeat = True
    while repeat:
        if len(deck2) <= n - 1:
            x = random.choice(symbols)
            if x not in deck2:
                deck2.append(x)
        else:
            repeat = False
    return deck2


comm = sys.argv
n = None
try:
    n = int(comm[1])
except:
    print("Számot adj meg!")
symbols = [y for y in range(100)]
deck1 = first_row(n, symbols)
conv = ' '.join(str(x) for x in deck1)
print(conv)
deck2 = second_row(n, deck1)
conv = ' '.join(str(x) for x in deck2)
print(conv)

for i in range(52):
    deck1 = game(deck1, deck2)
    conv = ' '.join(str(x) for x in deck1)
    print(conv)
    deck2 = game2(deck1, deck2)
    conv = ' '.join(str(x) for x in deck2)
    print(conv)