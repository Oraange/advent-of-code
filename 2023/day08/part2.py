import os
from math import lcm

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read()


def parse_input(datas: str):
    guide, map_ = datas.split("\n\n")
    map_ = map_.splitlines()
    return guide, map_


def get_step(src: str):
    step = 0

    while not src.endswith("Z"):
        src = m[src][dirct[guide[step % len(guide)]]]
        step += 1

    return step


dirct = {"L": 0, "R": 1}

guide, map_ = parse_input(datas)
m = {}

for line in map_:
    src, dest = line.split(" = ")
    m[src.strip()] = dest[1:-1].split(", ")

start_list = list(filter(lambda x: x.endswith("A"), m.keys()))

ans = lcm(*[get_step(start) for start in start_list])
print(ans)
