from functools import cache


def main(lines: str):
    stones = lines.split()

    @cache
    def count(v: str, rest: int) -> int:
        if rest == 0:
            return 1

        if v == "0":
            return count("1", rest - 1)

        elif len(v) % 2 == 0:
            mid = len(v) // 2
            l, r = v[:mid], v[mid:]
            return count(l, rest - 1) + count(r, rest - 1)
        else:
            return count(str(int(v) * 2024), rest - 1)

    res = 0
    for stone in stones:
        res += count(stone, 75)

    return res


if __name__ == "__main__":
    with open("2024/day11/test.txt", "r") as f:
        lines = f.read().strip()
    print(main(lines))
