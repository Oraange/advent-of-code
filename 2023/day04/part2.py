import os


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    datas = f.read().splitlines()


def parse_data(data):
    data = data.split(":")[-1].strip()
    wins, choices = data.split("|")
    wins = wins.split()
    choices = choices.split()
    return wins, choices


cards = [1 for _ in range(len(datas))]

for i, data in enumerate(datas):
    wins, choices = parse_data(data)
    matched = 0
    for choice in choices:
        if choice in wins:
            matched += 1

    for j in range(i + 1, i + 1 + matched):
        if j < len(cards):
            cards[j] += cards[i]

print(sum(cards))
