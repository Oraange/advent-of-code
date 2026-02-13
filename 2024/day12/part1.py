def main(lines: str):
    lines = lines.splitlines()
    ans = 0
    n = len(lines)
    m = len(lines[0])
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y, flw):
        if x < 0 or x >= n:
            garden[1] += 1

        if y < 0 or y >= m:
            garden[1] += 1

        if x < 0 or x >= n or y < 0 or y >= m:
            return

        if lines[x][y] != flw:
            garden[1] += 1
            return

        if visited[x][y]:
            return

        visited[x][y] = True
        garden[0] += 1

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dfs(x + dx, y + dy, lines[x][y])

    for i in range(n):
        for j in range(m):
            garden = [0, 0]
            dfs(i, j, lines[i][j])
            ans += garden[0] * garden[1]

    return ans


if __name__ == "__main__":
    with open("2024/day12/input.txt", "r") as f:
        lines = f.read().strip()
    print(main(lines))
