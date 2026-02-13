def main(datas: str):
    def dfs(node):
        nonlocal ans
        if "out" in graph[node]:
            ans += 1
            return

        for path in graph[node]:
            if path in graph:
                dfs(path)

    graph = {}
    ans = 0

    for data in datas.splitlines():
        k, v = data.split(": ")
        graph[k] = v.split()

    dfs("svr")
    return ans


if __name__ == "__main__":
    with open("2025/day11/input.txt", "r", encoding="utf-8") as f:
        datas = f.read().strip()
    print(main(datas))
