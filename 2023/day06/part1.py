import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    times, distances = f.read().splitlines()

times = list(map(int, times.split()[1:]))
distances = list(map(int, distances.split()[1:]))

ans = 1

for time, dist in zip(times, distances):
    res = 0
    for i in range(1, time):
        if i * (time - i) > dist:
            res += 1

    ans *= res

print(ans)
