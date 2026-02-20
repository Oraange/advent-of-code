from collections import deque


def main(data):
    maze = data.splitlines()
    n, m = len(maze), len(maze[0])
    rot = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                start = (i, j)
            if maze[i][j] == "E":
                end = (i, j)
        if "start" in locals() and "end" in locals():
            break

    q = deque([(start[0], start[1], rot)])
    visited = set([(start[0], start[1], rot)])
    minimum_root = [[float("inf")] * m for _ in range(n)]
    minimum_root[start[0]][start[1]] = 0
    while q:
        r, c, rot = q.popleft()
        if (r, c) == end:
            continue

        for i in range(len(directions)):
            dr, dc = directions[i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != "#":
                new_rot = i
                is_rot = rot != new_rot
                if (nr, nc, new_rot) in visited:
                    if minimum_root[nr][nc] > minimum_root[r][c] + (
                        1 if not is_rot else 1001
                    ):
                        minimum_root[nr][nc] = minimum_root[r][c] + (
                            1 if not is_rot else 1001
                        )
                    else:
                        continue
                visited.add((nr, nc, new_rot))
                q.append((nr, nc, new_rot))

    return minimum_root[end[0]][end[1]]


if __name__ == "__main__":
    with open("2024/day16/test1.txt", "r") as f:
        data = f.read()

    print(main(data))
