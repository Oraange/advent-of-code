from collections import Counter


def main(filename: str):
    with open(filename, "r") as f:
        lines = f.read().strip().splitlines()

    left = []
    right = []

    for line in lines:
        l, r = line.split()
        left.append(l)
        right.append(r)

    ans = 0

    rc = Counter(right)
    for lft in left:
        if lft in rc:
            ans += int(lft) * rc[lft]

    return ans


if __name__ == "__main__":
    print(main("2024/day01/input.txt"))
