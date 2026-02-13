import heapq as hq
from collections import Counter
from functools import reduce
from operator import mul

def main(pos_list: str):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parent[b] = a
        else:
            parent[a] = b
    pos_list = pos_list.splitlines()
    pos_list = [tuple(map(int, p.split(','))) for p in pos_list]

    n = len(pos_list)
    parent = [i for i in range(n)]
    hp = []
    get_dist = lambda a,b: sum((d1-d2)**2 for d1, d2 in zip(a, b))

    for i in range(n):
        for j in range(i+1, n):
            hq.heappush(hp, (get_dist(pos_list[i], pos_list[j]), i, j))

    for _ in range(1000):
        _, a, b = hq.heappop(hp)
        union(a, b)

    for i in range(1000):
        find(i)

    c = Counter(parent)
    return reduce(mul, [x[1] for x in c.most_common(3)])
