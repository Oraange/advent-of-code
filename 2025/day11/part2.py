from collections import deque


def main(datas: str):
    def dfs(node: str, is_fft: bool, is_dac: bool):
        if node == "fft":
            is_fft = True
        if node == "dac":
            is_dac = True

        state = (node, is_fft, is_dac)

        if state in visited:
            return visited[state]

        if node == "out":
            if is_fft and is_dac:
                return 1

            else:
                return 0

        path_count = 0

        for path in graph[node]:
            path_count += dfs(path, is_fft, is_dac)

        visited[state] = path_count
        return path_count

    graph = {}
    visited = {}
    ans = 0
    q = deque()
    is_fft = is_dac = False
    q.append(["svr", is_fft, is_dac])

    for data in datas.splitlines():
        k, v = data.split(": ")
        graph[k] = v.split()

    # while q:
    #     node, fft, dac = q.popleft()
    #     visited.add(node)

    #     if node not in graph:
    #         if node == "out":
    #             if fft and dac:
    #                 ans += 1

    #         continue

    #     if node == "fft":
    #         fft = True

    #     if node == "dac":
    #         dac = True

    #     for path in graph[node]:
    #         if node not in visited:
    #             q.append([path, fft, dac])

    # return ans

    return dfs("svr", False, False)


if __name__ == "__main__":
    with open("2025/day11/input.txt", "r", encoding="utf-8") as f:
        datas = f.read().strip()
    print(main(datas))
