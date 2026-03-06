from collections import deque
from functools import cache

keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

dirpad = [[None, "^", "A"], ["<", "v", ">"]]

dirs = [(0, 1, ">"), (1, 0, "v"), (0, -1, "<"), (-1, 0, "^")]


def positions(pad):
    return {
        pad[r][c]: (r, c)
        for r in range(len(pad))
        for c in range(len(pad[0]))
        if pad[r][c]
    }


def all_paths(pad):

    pos = positions(pad)
    paths = {}

    for s, (sr, sc) in pos.items():

        q = deque([(sr, sc, "")])
        best = {(sr, sc): 0}
        res = {}

        while q:
            r, c, p = q.popleft()

            if pad[r][c]:
                res.setdefault(pad[r][c], []).append(p)

            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(pad) and 0 <= nc < len(pad[0]) and pad[nr][nc]:

                    np = p + ch
                    if (nr, nc) not in best or len(np) <= best[(nr, nc)]:
                        best[(nr, nc)] = len(np)
                        q.append((nr, nc, np))

        paths[s] = res

    return paths


key_paths = all_paths(keypad)
dir_paths = all_paths(dirpad)


@cache
def cost(depth, s, e):

    best = float("inf")

    for p in dir_paths[s][e]:

        seq = p + "A"

        if depth == 1:
            best = min(best, len(seq))
        else:
            cur = "A"
            total = 0

            for c in seq:
                total += cost(depth - 1, cur, c)
                cur = c

            best = min(best, total)

    return best


def solve_code(code, robots):

    seq = "A" + code
    total = 0

    for i in range(len(seq) - 1):

        best = float("inf")

        for p in key_paths[seq[i]][seq[i + 1]]:

            cur = "A"
            cost_sum = 0

            for c in p + "A":
                cost_sum += cost(robots, cur, c)
                cur = c

            best = min(best, cost_sum)

        total += best

    return total * int(code[:-1])


def solve(data, robots):

    return sum(solve_code(line.strip(), robots) for line in data.splitlines())


if __name__ == "__main__":

    with open("2024/day21/input.txt") as f:
        data = f.read()

    print("Part1:", solve(data, 2))
    print("Part2:", solve(data, 25))
