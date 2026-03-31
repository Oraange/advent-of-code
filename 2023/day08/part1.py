import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read()


def parse_input(datas: str):
    guide, map_ = datas.split("\n\n")
    map_ = map_.splitlines()
    return guide, map_


dirct = {"L": 0, "R": 1}

guide, map_ = parse_input(datas)
m = {}

for line in map_:
    src, dest = line.split(" = ")
    m[src.strip()] = dest[1:-1].split(", ")

i = 0
cur = "AAA"

while cur != "ZZZ":
    cur = m[cur][dirct[guide[i % len(guide)]]]
    i += 1

print(i)
