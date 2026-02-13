def main(robot_info: str):
    infos = robot_info.splitlines()
    robot_map = [[0] * 101 for _ in range(103)]
    for info in infos:
        p, v = info.split()
        px, py = tuple(map(int, p[2:].split(",")))
        vx, vy = tuple(map(int, v[2:].split(",")))

        robot_map[(py + vy * 100) % 103][(px + vx * 100) % 101] += 1

    qud = [0, 0, 0, 0]
    for j in range(103):
        if j < 51:
            qud[0] += sum(robot_map[j][:50])
            qud[1] += sum(robot_map[j][51:])
        elif j > 51:
            qud[2] += sum(robot_map[j][:50])
            qud[3] += sum(robot_map[j][51:])

    ans = 1

    for q in qud:
        ans *= q

    return ans


if __name__ == "__main__":
    with open("2024/day14/input.txt", "r") as f:
        robot_info = f.read()
    print(main(robot_info))
