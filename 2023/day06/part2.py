import os

with open(os.path.join(os.path.dirname(__file__), "test.txt")) as f:
    times, distances = f.read().splitlines()

time = int("".join(times.split()[1:]))
distance = int("".join(distances.split()[1:]))
half_time = time // 2

l = 0
r = half_time

while l < r:
    mid = (l + r) // 2
    cur_dist = mid * (time - mid)

    if cur_dist > distance:
        r = mid
    elif cur_dist < distance:
        l = mid + 1
    else:
        break

print((half_time - mid + 1) * 2 - (not time % 2))
