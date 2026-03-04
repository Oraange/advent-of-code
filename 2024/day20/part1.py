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

cheat = ((0, -2), (-1, -1), (-2, 0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1))
ans = 0
for px, py in path:
    for dx, dy in cheat:
        nx, ny = px + dx, py + dy
        if (
            0 <= nx < n
            and 0 <= ny < n
            and data[nx][ny] in (".", "E")
            and time[(nx, ny)] - 2 > time[(px, py)]
        ):
            ans += time[(nx, ny)] - 2 - time[(px, py)] >= 100

print(ans)
