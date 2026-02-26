import os
from collections import deque


def parse_data(data):
    return [tuple(map(int, line.split(","))) for line in data.splitlines()]


def main(data: str, size: int, limit: int):
    data = parse_data(data)
    ram = [[float("inf")] * size for _ in range(size)]
    ram[0][0] = 0
    for idx in range(limit):
        x, y = data[idx]
        ram[y][x] = "#"

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and ram[ny][nx] != "#":
                if ram[ny][nx] > ram[y][x] + 1:
                    ram[ny][nx] = ram[y][x] + 1
                    q.append((nx, ny))

    return ram[size - 1][size - 1]


if __name__ == "__main__":
    with open("2024/day18/input.txt", "r") as f:
        data = f.read()

    if os.path.basename(f.name).startswith("test"):
        print(main(data, 7, 12))
    elif os.path.basename(f.name).startswith("input"):
        print(main(data, 71, 1024))
