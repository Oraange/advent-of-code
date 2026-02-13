import re


def main(lines: str):
    with open(lines, "r") as f:
        lines = f.read().strip()
    pttrn = r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))"
    res = re.findall(pttrn, lines)
    print(res)

    do = True
    ans = 0
    for r in res:
        if r == "do()":
            do = True
            continue

        elif r == "don't()":
            do = False
            continue

        if not do:
            continue

        a, b = r[4:-1].split(",")
        ans += int(a) * int(b)

    return ans


if __name__ == "__main__":
    print(main("2024/day03/input.txt"))
