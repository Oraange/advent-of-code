import heapq as hq

def main(txt_path: str):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return False
        if a > b:
            parent[b] = a
        else:
            parent[a] = b

        return True
    
    with open(txt_path, 'r') as f:
        pos_list = f.read()

    pos_list = pos_list.splitlines()
    pos_list = [tuple(map(int, p.split(','))) for p in pos_list]

    n = len(pos_list)
    comp = n
    parent = [i for i in range(n)]
    hp = []
    get_dist = lambda a,b: sum((d1-d2)**2 for d1, d2 in zip(a, b))

    for i in range(n):
        for j in range(i+1, n):
            hq.heappush(hp, (get_dist(pos_list[i], pos_list[j]), i, j))

    last_a = last_b = -1

    while comp > 1:
        _, a, b = hq.heappop(hp)
        if union(a, b):
            comp -= 1
            last_a, last_b = a, b

    return pos_list[last_a][0] * pos_list[last_b][0]

if __name__ == '__main__':
    print(main('input_eg.txt'))