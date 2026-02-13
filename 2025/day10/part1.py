from collections import deque


def parse_data(data: str):
    data = data.split()
    target_map = data[0][1:-1]
    btn_map = [tuple(map(int, prs[1:-1].split(","))) for prs in data[1:-1]]
    target = sum(2 ** i if target_map[i] == "#" else 0 for i in range(len(target_map)))

    def to_int(btns):
        num = 0
        for bnt in btns:
            num += 2**bnt

        return num

    int_btn = list(map(to_int, btn_map))
    return target, int_btn, len(target_map)


def bfs(target, btns, n):
    MAX = 1 << n
    visited = [-1] * MAX

    dq = deque()
    dq.append(0)
    visited[0] = 0

    while dq:
        cur = dq.popleft()

        if cur == target:
            return visited[cur]

        for b in btns:
            nxt = cur ^ b
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                dq.append(nxt)


def main(datas: str):
    ans = 0

    for data in datas.splitlines():
        target, btn_list, n = parse_data(data)
        ans += bfs(target, btn_list, n)

    return ans


if __name__ == "__main__":
    with open("2025/day10/input.txt", "r", encoding="utf-8") as f:
        datas = f.read().strip()
    print(main(datas))
