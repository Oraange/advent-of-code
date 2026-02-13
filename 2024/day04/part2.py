def match_x_mas(row, col, mat):
    return mat[row - 1][col - 1] + mat[row + 1][col + 1] in ("MS", "SM") and mat[
        row + 1
    ][col - 1] + mat[row - 1][col + 1] in ("MS", "SM")


def main(lines: str):
    with open(lines, "r") as f:
        lines = f.read().strip().splitlines()
    ans = 0
    n = len(lines)
    m = len(lines[0])
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            if lines[r][c] == "A":
                ans += match_x_mas(r, c, lines)

    return ans


if __name__ == "__main__":
    print(main("2024/day04/input.txt"))
