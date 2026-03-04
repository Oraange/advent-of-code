def parse_data(data: str):
    pttns, dsgns = data.split("\n\n")
    pttns = pttns.split(",")
    dsgns = dsgns.splitlines()

    return pttns, dsgns


def dfs(cur_pt, patterns, design):
    if cur_pt == design:
        return True

    for pattern in patterns:
        if design[len(cur_pt) : len(cur_pt) + len(pattern)] == pattern:
            if dfs(cur_pt + pattern, patterns, design):
                return True

    return False


def main(data):
    patterns, designs = parse_data(data)
    patterns = list(map(lambda x: x.strip(), patterns))
    cnt = 0
    for design in designs:
        cnt += dfs("", patterns, design)

    return cnt


if __name__ == "__main__":
    with open("2024/day19/input.txt", "r") as f:
        data = f.read()

    print(main(data))
