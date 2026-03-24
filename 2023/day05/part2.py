import os


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().split("\n\n")

seeds = list(map(int, datas[0][datas[0].index(":") + 1 :].split()))


def get_ranges(seeds):
    rng_list = []
    for i in range(0, len(seeds), 2):
        rng_list.append(range(seeds[i], seeds[i] + seeds[i + 1]))

    return rng_list


def get_dest(seed, src, dest, rng):
    if dest <= seed < dest + rng:
        return seed + src - dest


def parse_data(data: str):
    mapping_lines = data.splitlines()[1:]
    for i in range(len(mapping_lines)):
        mapping_lines[i] = list(map(int, mapping_lines[i].split()))

    return mapping_lines


_map = []

for data in datas[1:]:
    _map.append(parse_data(data))

ans = float("inf")

for rng in get_ranges(seeds):
    for seed in rng:
        src = seed
        for i, m in enumerate(_map):
            for l in m:
                if l[1] <= src < l[1] + l[2]:
                    src += l[0] - l[1]
                    break
        ans = min(ans, src)

print(ans)
