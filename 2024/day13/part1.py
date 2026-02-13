import numpy as np
import re


def parse_input(attempt: str):
    attempt = attempt.strip().splitlines()
    AX, AY = list(map(int, re.findall(r"\d+", attempt[0])))
    BX, BY = list(map(int, re.findall(r"\d+", attempt[1])))
    prize = list(map(int, re.findall(r"\d+", attempt[2])))
    return [AX, BX], [AY, BY], prize


def main(datas: str):
    attempts = datas.strip().split("\n\n")
    ans = 0
    cnt = 0
    for attempt in attempts:
        cnt += 1
        X, Y, PRIZE = parse_input(attempt)
        if X[0] * Y[1] == X[1] * Y[0]:
            if PRIZE[0] * Y[1] == PRIZE[1] * Y[0]:
                total_prize = float("inf")
                t = PRIZE[0] // X[1]
                print(f"{cnt} | Infinitely many solutions")
                for i in range(t, -1, -1):
                    if (PRIZE[0] - i * X[1]) % X[0] == 0:
                        a = (PRIZE[0] - i * X[1]) // X[0]
                        b = i
                        total_prize = min(total_prize, 3 * a + b)
            else:
                print(f"{cnt} | No solution")
                continue
        else:
            sol = np.linalg.solve(np.array([X, Y]), np.array(PRIZE))
            print(f"Solution: {sol}")
            for s in sol:
                print(f"{s}", end=" ")
            if all(s.is_integer() and s >= 0 for s in sol):
                print(f"{cnt} | Unique solution")
                total_prize = 3 * sol[0] + sol[1]
            else:
                print(f"{cnt} | No solution")
                continue

        print(f"Total prize: {total_prize}")
        ans += int(total_prize)
    return ans


if __name__ == "__main__":
    with open("2024/day13/test.txt", "r") as f:
        datas = f.read()
    print(main(datas))
