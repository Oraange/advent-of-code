def parse_input(data):
    _, operations = data.split("\n\n")
    program = list(map(int, operations[operations.index(":") + 1 :].split(",")))
    return program


def run(A):
    B = 0
    C = 0
    out = []

    while A != 0:
        B = A % 8
        B ^= 3
        C = A >> B
        B ^= C
        B ^= 3
        out.append(B % 8)
        A >>= 3

    return out


def main(data):
    data = parse_input(data)
    candidates = {0}

    for i in range(len(data) - 1, -1, -1):
        new = set()
        for base in candidates:
            for low in range(8):
                A = (base << 3) | low
                if run(A)[: len(data) - i] == data[i:]:
                    new.add(A)
        candidates = new

    return min(candidates)


if __name__ == "__main__":
    with open("2024/day17/input.txt", "r") as f:
        data = f.read()
    print(main(data))
