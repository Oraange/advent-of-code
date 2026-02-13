def get_grid(lines: str):
    lines = lines.splitlines()
    n = len(lines)
    m = len(lines[0])
    grid = [[""] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = lines[i][j]
    return grid


def main(grid):
    R, C = len(grid), len(grid[0])

    # 방향: 위, 오른쪽, 아래, 왼쪽
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 시작 위치와 방향 찾기
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "^":
                sr, sc = r, c
                sd = 0  # '^'는 위
                break

    def causes_loop(block_r, block_c):
        r, c, d = sr, sc, sd
        visited = set()

        while True:
            state = (r, c, d)
            if state in visited:
                return True  # 루프 발생
            visited.add(state)

            nr = r + dr[d]
            nc = c + dc[d]

            # 맵 밖 → 탈출 (루프 아님)
            if not (0 <= nr < R and 0 <= nc < C):
                return False

            # 장애물 (# 또는 새로 놓은 block) → 회전
            if grid[nr][nc] == "#" or (nr == block_r and nc == block_c):
                d = (d + 1) % 4
            else:
                r, c = nr, nc

    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "." and (r, c) != (sr, sc):
                if causes_loop(r, c):
                    count += 1

    return count


if __name__ == "__main__":
    with open("2024/day06/input.txt", "r") as f:
        lines = f.read().strip()
    grid = get_grid(lines)
    print(main(grid))
