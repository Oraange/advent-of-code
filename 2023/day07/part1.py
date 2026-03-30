import os
from collections import Counter
from functools import cmp_to_key

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().splitlines()

order = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

datas = list(map(lambda x: x.split(), datas))


def hand_ranking(hand):
    c = Counter(hand).most_common()

    if c[0][1] == 5:
        return "FIVE CARD!!!!!"
    elif c[0][1] == 4:
        return "FOUR CARD!!!!"
    elif c[0][1] == 3:
        if c[1][1] == 2:
            return "FULL HOUSE!!!"
        else:
            return "TRIPLE!!!"
    elif c[0][1] == 2:
        if c[1][1] == 2:
            return "TWO PAIR!!"
        else:
            return "ONE PAIR!"
    else:
        return "NO CARD"


def comp(x, y):
    x = x[0]
    y = y[0]
    cx = Counter(x).most_common()
    cy = Counter(y).most_common()
    for a, b in zip(cx, cy):
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -1
    for i in range(5):
        if order.index(x[i]) > order.index(y[i]):
            return 1
        elif order.index(x[i]) < order.index(y[i]):
            return -1
    return 0


datas.sort(key=cmp_to_key(comp))

ans = 0

for rank, data in enumerate(datas, start=1):
    hand, bid = data
    ans += int(bid) * rank

print(ans)
