from collections import deque, defaultdict


def solve(grid):
    R = len(grid)
    C = len(grid[0])
    visited = [[False] * C for _ in range(R)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    total_price = 0

    for r in range(R):
        for c in range(C):
            if visited[r][c]:
                continue

            plant = grid[r][c]
            queue = deque([(r, c)])
            visited[r][c] = True
            region = [(r, c)]

            # --- BFS로 region 찾기 ---
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if not visited[nr][nc] and grid[nr][nc] == plant:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            region.append((nr, nc))

            area = len(region)

            # --- boundary edge 모으기 ---
            top_edges = defaultdict(list)
            bottom_edges = defaultdict(list)
            left_edges = defaultdict(list)
            right_edges = defaultdict(list)

            for cr, cc in region:
                # 위
                if cr == 0 or grid[cr - 1][cc] != plant:
                    top_edges[cr].append(cc)

                # 아래
                if cr == R - 1 or grid[cr + 1][cc] != plant:
                    bottom_edges[cr].append(cc)

                # 왼쪽
                if cc == 0 or grid[cr][cc - 1] != plant:
                    left_edges[cc].append(cr)

                # 오른쪽
                if cc == C - 1 or grid[cr][cc + 1] != plant:
                    right_edges[cc].append(cr)

            # --- 연속 edge 묶어서 side 계산 ---
            def count_sides(edge_dict):
                sides = 0
                for key in edge_dict:
                    arr = sorted(edge_dict[key])
                    prev = arr[0]
                    sides += 1
                    for i in range(1, len(arr)):
                        if arr[i] != prev + 1:
                            sides += 1
                        prev = arr[i]
                return sides

            sides = (
                count_sides(top_edges)
                + count_sides(bottom_edges)
                + count_sides(left_edges)
                + count_sides(right_edges)
            )

            total_price += area * sides

    return total_price


if __name__ == "__main__":
    with open("2024/day12/input.txt", "r") as f:
        lines = f.read().strip().splitlines()

    grid = [list(line) for line in lines]
    result = solve(grid)
    print(result)
