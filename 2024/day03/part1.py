import re


def main(lines: str):
    with open(lines, "r") as f:
        lines = f.read().strip()
    pttrn = r"mul\(\d+,\d+\)"
    res = re.findall(pttrn, lines)

    ans = 0
    for r in res:
        a, b = r[4:-1].split(",")
        ans += int(a) * int(b)

    return ans


if __name__ == "__main__":
    print(main("2024/day03/input.txt"))
