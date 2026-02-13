import time


def main(robot_info: str):
    infos = robot_info.splitlines()
    robot_map = [[0] * 101 for _ in range(103)]
    pos = []

    for info in infos:
        p, v = info.split()
        px, py = tuple(map(int, p[2:].split(",")))
        vx, vy = tuple(map(int, v[2:].split(",")))

        robot_map[(py + vy * 100) % 103][(px + vx * 100) % 101] += 1
        pos.append(((px, py), (vx, vy)))

    tic = 0

    while True:
        for robot in robot_map:
            print(robot)
        time.sleep(1)
        tic += 1


if __name__ == "__main__":
    with open("2024/day14/input.txt", "r") as f:
        robot_info = f.read()
    print(main(robot_info))
