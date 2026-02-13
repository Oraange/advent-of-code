import numpy as np
import re


def parse_input(attempt: str):
    attempt = attempt.strip().splitlines()
    AX, AY = list(map(int, re.findall(r"\d+", attempt[0])))
    BX, BY = list(map(int, re.findall(r"\d+", attempt[1])))
    prize = list(map(int, re.findall(r"\d+", attempt[2])))
    prize[0] += 10000000000000
    prize[1] += 10000000000000
    return [AX, BX], [AY, BY], prize


def main(datas: str):
    attempts = datas.strip().split("\n\n")
    ans = 0
    for attempt in attempts:
        X, Y, PRIZE = parse_input(attempt)
        det = X[0] * Y[1] - X[1] * Y[0]
        if det == 0:
            if PRIZE[0] * Y[1] == PRIZE[1] * X[1]:
                total_prize = float("inf")
                t = PRIZE[0] // X[1]
                for i in range(t, -1, -1):
                    if (PRIZE[0] - i * X[1]) % X[0] == 0:
                        a = (PRIZE[0] - i * X[1]) // X[0]
                        b = i
                        total_prize = min(total_prize, 3 * a + b)
            else:
                continue
        else:
            sol_x, sol_y = (
                (Y[1] * PRIZE[0] - X[1] * PRIZE[1]) / det,
                (-Y[0] * PRIZE[0] + X[0] * PRIZE[1]) / det,
            )
            if sol_x >= 0 and sol_y >= 0 and sol_x.is_integer() and sol_y.is_integer():
                total_prize = 3 * int(sol_x) + int(sol_y)
            else:
                continue

        ans += int(total_prize)
    return ans


if __name__ == "__main__":
    with open("2024/day13/input.txt", "r") as f:
        datas = f.read()
    print(main(datas))
