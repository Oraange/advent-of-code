import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().strip().splitlines()

ans = 0

for line in lines:
    num = 0
    i, j = 0, len(line) - 1
    stop_i = stop_j = False
    while i <= j:
        if not stop_i and line[i].isdigit():
            num += 10 * int(line[i])
            stop_i = True
        if not stop_j and line[j].isdigit():
            num += int(line[j])
            stop_j = True

        if stop_i and stop_j:
            break

        i += not stop_i
        j -= not stop_j

    ans += num

print(ans)
