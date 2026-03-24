import os


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().splitlines()


def parse_data(data):
    data = data.split(":")[-1].strip()
    wins, choices = data.split("|")
    wins = wins.split()
    choices = choices.split()
    return wins, choices


ans = 0

for data in datas:
    wins, choices = parse_data(data)
    matched = 0
    for choice in choices:
        if choice in wins:
            matched += 1

    ans += pow(2, (matched - 1)) if matched > 0 else 0

print(ans)
