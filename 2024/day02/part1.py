def main(filename: str):
    with open(filename, "r") as f:
        lines = f.read().strip().splitlines()

    ans = 0
    for line in lines:
        report = list(map(int, line.split()))
        ans += all(
            1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report))
        ) or all(1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report)))

    return ans


if __name__ == "__main__":
    print(main("2024/day02/input.txt"))
