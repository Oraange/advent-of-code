import pulp


def min_presses(target: tuple[int, int, int], vectors: list[tuple[int, int, int]]):
    n = len(target)
    m = len(vectors)

    prob = pulp.LpProblem("Factory", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(m)]

    prob += pulp.lpSum(x)

    for i in range(n):
        prob += pulp.lpSum(x[j] for j in range(m) if i in vectors[j]) == target[i]

    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[status] != "Optimal":
        return float("inf")

    return int(pulp.value(prob.objective))


def parse_data(data: str):
    data = data.split()
    vectors, target = data[1:-1], data[-1]
    vectors = [list(map(int, t[1:-1].split(","))) for t in vectors]
    target = tuple(map(int, target[1:-1].split(",")))

    return vectors, target


def main(datas: str):
    ans = 0
    datas = datas.splitlines()
    for data in datas:
        vectors, target = parse_data(data)
        each_ans = min_presses(target, vectors)
        ans += each_ans

    return ans


if __name__ == "__main__":
    with open("2025/day10/input.txt", "r", encoding="utf-8") as f:
        datas = f.read().strip()
    print(main(datas))
