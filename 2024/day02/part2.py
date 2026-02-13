def is_valid_report(report: list):
    if all(1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report))) or all(
        1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report))
    ):
        return True

    return False


def main(lines: str):
    with open(lines, "r") as f:
        lines = f.read().strip().splitlines()
    ans = 0
    for line in lines:
        report = list(map(int, line.split()))
        ans += any(
            is_valid_report(report[:i] + report[i + 1 :]) for i in range(len(report))
        )

    return ans


if __name__ == "__main__":
    print(main("2024/day02/input.txt"))
