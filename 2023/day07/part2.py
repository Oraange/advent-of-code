import os
from collections import Counter
from functools import cmp_to_key

with open(os.path.join(os.path.dirname(__file__), "test.txt")) as f:
    datas = f.read().splitlines()

ans = 0
order = ("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")
datas = list(map(lambda x: x.split(), datas))


def get_count(hand):
    most = list(map(list, Counter(hand).most_common()))
    if most[0][0] == "J":
        if most[0][1] != 5:
            most[1][1] += most[0][1]
            del most[0]
    else:
        for i in range(1, len(most)):
            if most[i][0] == "J":
                most[0][1] += most[i][1]
                del most[i]
                break

    return most


def comp(x, y):
    x = x[0]
    y = y[0]
    cx = get_count(x)
    cy = get_count(y)

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

for rank, data in enumerate(datas, start=1):
    hand, bid = data
    ans += int(bid) * rank

print(ans)
