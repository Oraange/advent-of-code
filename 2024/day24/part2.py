import os
import re
from collections import defaultdict


def solve(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f if l.strip()]

    gates = []
    for line in lines:
        if ":" in line:
            continue

        a, op, b, _, out = line.split()
        gates.append((a, op, b, out))

    wrong = set()

    for a, op, b, out in gates:

        # 규칙 1
        # z는 마지막 비트를 제외하고 XOR이어야 한다
        if out.startswith("z") and op != "XOR" and out != "z45":
            wrong.add(out)

        # 규칙 2
        # XOR gate는 x,y,z 중 하나와 연결되어야 한다
        if op == "XOR":
            if not (
                a.startswith(("x", "y", "z"))
                or b.startswith(("x", "y", "z"))
                or out.startswith(("x", "y", "z"))
            ):
                wrong.add(out)

        # 규칙 3
        # AND는 대부분 carry 계산용이라 OR로 이어져야 한다
        if op == "AND":
            if a != "x00" and b != "x00":
                used_in_or = False
                for aa, oop, bb, oout in gates:
                    if (aa == out or bb == out) and oop == "OR":
                        used_in_or = True
                if not used_in_or:
                    wrong.add(out)

        # 규칙 4
        # XOR 결과가 다시 XOR로 연결되지 않으면 이상
        if op == "XOR":
            used = False
            for aa, oop, bb, oout in gates:
                if aa == out or bb == out:
                    if oop == "XOR":
                        used = True
            if not used and not out.startswith("z"):
                wrong.add(out)

    ans = sorted(wrong)
    print(",".join(ans))


solve(os.path.join(os.path.dirname(__file__), "input.txt"))
