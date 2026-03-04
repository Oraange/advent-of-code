with open("2024/day19/input.txt", "r") as f:
    data = f.read()

patterns, designs = data.split("\n\n")
patterns = list(map(lambda x: x.strip(), patterns.split(",")))
designs = designs.splitlines()


def dp(design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for e in range(1, n + 1):
        for pt in patterns:
            s = e - len(pt)
            if s < 0:
                continue
            if design[s:e] == pt:
                dp[e] += dp[s]

    return dp[n]


def main():
    cnt = 0
    for design in designs:
        cnt += dp(design)

    return cnt


if __name__ == "__main__":
    with open("2024/day19/test.txt", "r") as f:
        data = f.read()

    print(main())
