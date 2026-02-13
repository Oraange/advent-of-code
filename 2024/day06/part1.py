def main(lines: str):
    lines = lines.splitlines()
    n = len(lines)
    m = len(lines[0])
    cur_x, cur_y = 0, 0

    for i in range(n):
        j = lines[i].find("^")
        if j != -1:
            cur_x = i
            cur_y = j
        lines[i] = list(lines[i])

    ans = 0
    state = 0 % 4  # UP: 0 / RIGHT: 1 / DOWN: 2 / LEFT: 3

    while (0 <= cur_x < n) and (0 <= cur_y < m):
        if state == 0:
            while 0 < cur_x and lines[cur_x - 1][cur_y] != "#":
                if lines[cur_x][cur_y] != "X":
                    ans += 1
                    lines[cur_x][cur_y] = "X"
                cur_x -= 1

            if cur_x == 0:
                return ans + 1
            state = (state + 1) % 4

        elif state == 1:
            while cur_y < m - 1 and lines[cur_x][cur_y + 1] != "#":
                if lines[cur_x][cur_y] != "X":
                    ans += 1
                    lines[cur_x][cur_y] = "X"
                cur_y += 1

            if cur_y == m - 1:
                return ans + 1
            state = (state + 1) % 4

        elif state == 2:
            while cur_x < n - 1 and lines[cur_x + 1][cur_y] != "#":
                if lines[cur_x][cur_y] != "X":
                    ans += 1
                    lines[cur_x][cur_y] = "X"
                cur_x += 1

            if cur_x == n - 1:
                return ans + 1
            state = (state + 1) % 4

        else:
            while 0 < cur_y and lines[cur_x][cur_y - 1] != "#":
                if lines[cur_x][cur_y] != "X":
                    ans += 1
                    lines[cur_x][cur_y] = "X"
                cur_y -= 1

            if cur_y == 0:
                return ans + 1
            state = (state + 1) % 4

    return ans + 1


if __name__ == "__main__":
    with open("2024/day06/input.txt", "r") as f:
        lines = f.read().strip()
    print(main(lines))
