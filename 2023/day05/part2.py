import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().split("\n\n")


def solve(blocks):
    seeds = list(map(int, blocks[0].split(":")[1].split()))
    ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    maps = [
        [tuple(map(int, line.split())) for line in block.splitlines()[1:]]
        for block in blocks[1:]
    ]

    for rules in maps:
        new = []
        for start, end in ranges:
            stack = [(start, end)]
            for dst, src, length in rules:
                temp = []
                s0, s1 = src, src + length
                shift = dst - src
                for a, b in stack:
                    if b <= s0 or s1 <= a:
                        temp.append((a, b))
                    else:
                        if a < s0:
                            temp.append((a, s0))
                        new.append((max(a, s0) + shift, min(b, s1) + shift))
                        if s1 < b:
                            temp.append((s1, b))
                stack = temp
            new.extend(stack)
        ranges = new

    return min(s for s, _ in ranges)


print(solve(datas))
