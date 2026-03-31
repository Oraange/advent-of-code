import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().splitlines()


def find_sequence(seq: list):
    if not any(seq):
        return 0

    new_seq = [seq[i] - seq[i - 1] for i in range(1, len(seq))]

    next_val = seq[0] - find_sequence(new_seq)
    return next_val


ans = 0

for data in datas:
    data = list(map(int, data.split()))
    num = find_sequence(data)
    ans += num

print(ans)
