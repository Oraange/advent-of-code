def main(lines):
    with open(lines, "r") as f:
        lines = f.read().strip().splitlines()
    left = []
    right = []

    for line in lines:
        l, r = line.split()
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    return sum([abs(int(r_) - int(l_)) for l_, r_ in zip(left, right)])


if __name__ == "__main__":
    print(main("2024/day01/input.txt"))
