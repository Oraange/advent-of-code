def match_xmas(row, col, mat):
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
    matched = 0

    for x, y in direction:
        xmas = ""
        for ln in range(4):
            dx = row + ln * x
            dy = col + ln * y
            if 0 <= dx < len(mat) and 0 <= dy < len(mat[0]):
                xmas += mat[dx][dy]

        if xmas == "XMAS":
            matched += 1

    return matched


def main(lines: str):
    with open(lines, "r") as f:
        lines = f.read().strip().splitlines()
    ans = 0
    n = len(lines)
    m = len(lines[0])
    for r in range(n):
        for c in range(m):
            ans += match_xmas(r, c, lines)

    return ans


if __name__ == "__main__":
    print(main("2024/day04/input.txt"))
