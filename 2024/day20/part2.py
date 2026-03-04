with open("2024/day20/input.txt", "r") as f:
    data = f.read()

data = data.splitlines()
n = len(data)

for i in range(n):
    for j in range(n):
        if data[i][j] == "S":
            start = (i, j)
        if data[i][j] == "E":
            end = (i, j)

path = [start]
pico = 0
time = {start: pico}

while path[-1] != end:
    px, py = path[-1]
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = px + dx, py + dy
        if data[nx][ny] in (".", "E") and (nx, ny) not in path:
            path.append((nx, ny))
            pico += 1
            time[(nx, ny)] = pico
            break

ans = 0
MAX_CHEAT = 20
for px, py in path:
    for i in range(px - MAX_CHEAT, px + MAX_CHEAT + 1):
        for j in range(py - MAX_CHEAT, py + MAX_CHEAT + 1):
            used = abs(px - i) + abs(py - j)
            if (
                i < 0
                or i >= n
                or j < 0
                or j >= n
                or used > MAX_CHEAT
                or data[i][j] == "#"
            ):
                continue

            if time[(i, j)] - time[(px, py)] - used >= 100:
                ans += 1

print(ans)
