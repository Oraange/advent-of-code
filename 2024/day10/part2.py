from collections import deque


def main(lines: str):
    lines = lines.splitlines()
    ans = 0

    n = len(lines)
    m = len(lines[0])
    dir = ((1, 0), (0, 1), (-1, 0), (0, -1))

    for i in range(n):
        for j in range(m):
            cnt = 1
            if lines[i][j] == "0":
                cur_ans = 0
                dq = deque()
                dq.append((i, j))

                while dq:
                    cur_x, cur_y = dq.popleft()
                    for dx, dy in dir:
                        nxt_x, nxt_y = cur_x + dx, cur_y + dy
                        if 0 <= nxt_x < n and 0 <= nxt_y < m:
                            if int(lines[nxt_x][nxt_y]) == int(lines[cur_x][cur_y]) + 1:
                                if lines[nxt_x][nxt_y] == "9":
                                    cur_ans += 1
                                    continue
                                dq.append((nxt_x, nxt_y))

                ans += cur_ans
                cnt += 1

    return ans


if __name__ == "__main__":
    with open("2024/day10/input.txt", "r") as f:
        lines = f.read().strip()
    print(main(lines))
