from collections import deque

keypad = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [None, 0, "A"]]
dirpad = [[None, "^", "A"], ["<", "v", ">"]]
dir = {(0, 1): ">", (1, 0): "v", (0, -1): "<", (-1, 0): "^"}
key_pos = {}
dir_pos = {}

for r in range(len(keypad)):
    for c in range(len(keypad[0])):
        if keypad[r][c] is not None:
            key_pos[keypad[r][c]] = (r, c)

for r in range(len(dirpad)):
    for c in range(len(dirpad[0])):
        if dirpad[r][c] is not None:
            dir_pos[dirpad[r][c]] = (r, c)


def bfs(start, pad, pos):
    r, c = pos[start]
    q = deque([(r, c, "")])
    n = len(pad)
    m = len(pad[0])
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    paths = {}

    while q:
        x, y, path = q.popleft()
        current_value = pad[x][y]
        paths[current_value] = path
        for (dx, dy), d in dir.items():
            nx, ny = dx + x, dy + y

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and pad[nx][ny] is not None
            ):
                visited[nx][ny] = True
                q.append((nx, ny, path + d))

    return paths


def main(data):
    datas = data.splitlines()
    ans = 0
    all_key_paths = {}
    all_dir_paths = {}
    for s in key_pos.keys():
        all_key_paths[s] = bfs(s, keypad, key_pos)

    for s in dir_pos.keys():
        all_dir_paths[s] = bfs(s, dirpad, dir_pos)

    for data in datas:
        whole_path = ""
        data = list(map(lambda x: int(x) if x.isdigit() else x, data))
        data.insert(0, "A")
        cur = "A"
        for i in range(1, len(data)):
            n2n = all_key_paths[data[i - 1]][data[i]] + "A"
            print(f"{data[i-1]} -> {data[i]}: {n2n}")
            input_robot = ""
            for j in range(len(n2n)):
                cur2 = "A"
                input_robot += all_dir_paths[cur][n2n[j]] + "A"
                print(f"input_robot: {input_robot}")
                for k in range(len(input_robot)):
                    whole_path += all_dir_paths[cur2][input_robot[k]] + "A "
                    print(f"whole_path: {whole_path}")
                    cur2 = input_robot[k]
                cur = n2n[j]

        # print(f"whole_path: {whole_path}")
        print("================")


if __name__ == "__main__":
    with open("2024/day21/test.txt", "r") as f:
        data = f.read()

    main(data)
