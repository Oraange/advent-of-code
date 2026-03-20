import os

with open(os.path.join(os.path.dirname(__file__), "test.txt")) as f:
    schemes = f.read().splitlines()

n = len(schemes)
m = len(schemes[0])
ans = 0


def is_boundary(x, y):
    return 0 <= x < n and 0 <= y < m


def check_num(cx, cy, visited):
    if is_boundary(cx, cy) and schemes[cx][cy].isdigit() and (cx, cy) not in visited:
        visited.add((cx, cy))
        return schemes[cx][cy]

    return None


def get_num(px, py):
    visited = set()
    nums = []

    for dx, dy in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ):
        cx, cy = px + dx, py + dy
        tmp_num = ""
        if schemes[cx][cy].isdigit():
            while check_num(cx, cy, visited):
                tmp_num = check_num(cx, cy, visited) + tmp_num
                cy -= 1

            while check_num(cx, cy + 1, visited):
                tmp_num += check_num(cx, cy + 1, visited)
                cy += 1
        if tmp_num != "":
            nums.append(tmp_num)


def main(schm):
    for i in range(n):
        for j in range(m):
            ...
