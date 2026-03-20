import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().strip().splitlines()

ans = 0
str_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in lines:
    digit = []
    for i in range(len(line)):
        if line[i].isdigit():
            digit.append(int(line[i]))
        else:
            for key in str_to_int:
                if line[i:].startswith(key):
                    digit.append(str_to_int[key])

    ans += digit[0] * 10 + digit[-1]

print(ans)
