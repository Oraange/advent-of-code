import heapq
from collections import deque


def dijkstra(maze, start, end):
    n, m = len(maze), len(maze[0])
    start_dir = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dist = [[[float("inf")] * 4 for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]][start_dir] = 0
    visited = set()

    pq = [(0, start[0], start[1], start_dir)]

    while pq:
        cur_cost, r, c, rot = heapq.heappop(pq)
        if cur_cost != dist[r][c][rot]:
            continue
        if (r, c) == end:
            continue

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != "#":
                if abs(i - rot) == 2:
                    continue

                step_cost = 1 if rot == i else 1001
                next_cost = cur_cost + step_cost
                if next_cost < dist[nr][nc][i]:
                    dist[nr][nc][i] = next_cost
                    heapq.heappush(pq, (next_cost, nr, nc, i))

    q = deque(
        [
            (end[0], end[1], i)
            for i in range(4)
            if dist[end[0]][end[1]][i] == min(dist[end[0]][end[1]])
        ]
    )

    while q:
        r, c, rot = q.popleft()
        visited.add((r, c))

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r - dr, c - dc
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != "#":
                for j in range(4):
                    if dist[r][c][rot] == dist[nr][nc][j] + (1 if rot == j else 1001):
                        q.append((nr, nc, j))

    return len(visited)


def main(data):
    maze = data.splitlines()
    n, m = len(maze), len(maze[0])

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                start = (i, j)
            if maze[i][j] == "E":
                end = (i, j)
        if "start" in locals() and "end" in locals():
            break
    return dijkstra(maze, start, end)


if __name__ == "__main__":
    with open("2024/day16/input.txt", "r") as f:
        data = f.read()

    print(main(data))
