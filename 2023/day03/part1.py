import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    schemes = f.read().splitlines()

n = len(schemes)
m = len(schemes[0])
ans = 0


def get_num(i, j_start, j_end):
    for j in range(j_start, j_end + 1):
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
            cx, cy = i + dx, j + dy
            if (
                0 <= cx < n
                and 0 <= cy < m
                and not schemes[cx][cy].isdigit()
                and schemes[cx][cy] != "."
            ):
                return True

    return False


for i in range(n):
    num = ""
    for j in range(m):
        if schemes[i][j].isdigit():
            num += schemes[i][j]

        if j == m - 1 or not schemes[i][j].isdigit():
            if num != "":
                end = j if schemes[i][j].isdigit() else j - 1
                if get_num(i, end - len(num) + 1, end):
                    ans += int(num)
            num = ""

print(ans)
