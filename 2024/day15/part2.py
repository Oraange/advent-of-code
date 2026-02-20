from collections import deque


def parse(d: str):
    mp = []
    d, info = d.split("\n\n")
    for line in d.splitlines():
        tmp = []
        for obj in line:
            if obj == "@":
                tmp.append("@")
                tmp.append(".")
            elif obj == "O":
                tmp.append("[")
                tmp.append("]")
            else:
                tmp.append(obj)
                tmp.append(obj)
        mp.append(tmp)
    return mp, info


def get_object(mp, d, si, sj):
    n = len(mp)

    if si + d < 0 or si + d >= n or mp[si + d][sj] == "#":
        return None

    q = deque([(si + d, sj)])
    visited = {(si + d, sj)}

    while q:
        r, c = q.popleft()
        if mp[r][c] == "[":
            if (r, c + 1) not in visited:
                q.append((r, c + 1))
                visited.add((r, c + 1))
        elif mp[r][c] == "]":
            if (r, c - 1) not in visited:
                q.append((r, c - 1))
                visited.add((r, c - 1))
        if mp[r + d][c] in "[]":
            if (r + d, c) not in visited:
                q.append((r + d, c))
                visited.add((r + d, c))

    return visited


def can_move(mp, d, clst):
    for r, c in clst:
        nr = r + d
        if mp[nr][c] == "#":
            return False
        if mp[nr][c] in "[]" and (nr, c) not in clst:
            return False
    return True


def move_vertical(mp, d, clst, cx, cy):
    all_cells = set(clst)
    all_cells.add((cx, cy))

    for r, c in sorted(all_cells, reverse=d == 1):
        mp[r][c], mp[r + d][c] = mp[r + d][c], mp[r][c]

    mp[cx + d][cy] = "@"


def move_horizontal(mp, d, cx, cy):
    pnt = cy
    while mp[cx][pnt + d] in "[]" and 0 <= pnt + d < len(mp[0]):
        pnt += d

    if mp[cx][pnt + d] == "#":
        return False

    if d == -1:
        for c in range(pnt + d, cy):
            mp[cx][c], mp[cx][c + 1] = mp[cx][c + 1], mp[cx][c]
    else:
        for c in range(pnt + d, cy, -1):
            mp[cx][c], mp[cx][c - 1] = mp[cx][c - 1], mp[cx][c]

    return True


def main(data):
    mp, infos = parse(data)

    n = len(mp)
    m = len(mp[0])
    for i in range(n):
        for j in range(m):
            if mp[i][j] == "@":
                cur_x = i
                cur_y = j

    for info in infos:
        if info == "^":
            if mp[cur_x - 1][cur_y] == "#":
                continue
            if mp[cur_x - 1][cur_y] == ".":
                mp[cur_x - 1][cur_y] = "@"
                mp[cur_x][cur_y] = "."
                cur_x -= 1
                continue
            obj = get_object(mp, -1, cur_x, cur_y)
            if can_move(mp, -1, obj):
                move_vertical(mp, -1, obj, cur_x, cur_y)
                cur_x -= 1
        elif info == "v":
            if mp[cur_x + 1][cur_y] == "#":
                continue
            if mp[cur_x + 1][cur_y] == ".":
                mp[cur_x + 1][cur_y] = "@"
                mp[cur_x][cur_y] = "."
                cur_x += 1
                continue
            obj = get_object(mp, 1, cur_x, cur_y)
            if can_move(mp, 1, obj):
                move_vertical(mp, 1, obj, cur_x, cur_y)
                cur_x += 1
        elif info == "<":
            if mp[cur_x][cur_y - 1] == "#":
                continue
            if mp[cur_x][cur_y - 1] == ".":
                mp[cur_x][cur_y - 1] = "@"
                mp[cur_x][cur_y] = "."
                cur_y -= 1
                continue
            if move_horizontal(mp, -1, cur_x, cur_y):
                cur_y -= 1
        elif info == ">":
            if mp[cur_x][cur_y + 1] == "#":
                continue
            if mp[cur_x][cur_y + 1] == ".":
                mp[cur_x][cur_y + 1] = "@"
                mp[cur_x][cur_y] = "."
                cur_y += 1
                continue
            if move_horizontal(mp, 1, cur_x, cur_y):
                cur_y += 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if mp[i][j] == "[":
                ans += i * 100 + j

    return ans


if __name__ == "__main__":
    with open("2024/day15/input.txt", "r") as f:
        data = f.read()

    print(main(data))
