import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    schemes = f.read().splitlines()

n = len(schemes)
m = len(schemes[0])
ans = 0


def is_boundary(x, y):
    return 0 <= x < n and 0 <= y < m


def check_num(cx, cy, visited):
    if is_boundary(cx, cy) and schemes[cx][cy].isdigit() and (cx, cy) not in visited:
        visited.add((cx, cy))
        return True

    return False


def get_nums(px, py):
    visited = set()
    nums = []

    for dx, dy in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ):
        cx, cy = px + dx, py + dy
        tmp_num = ""
        if is_boundary(cx, cy) and schemes[cx][cy].isdigit():
            pivot = cy
            while check_num(cx, pivot, visited):
                tmp_num = schemes[cx][pivot] + tmp_num
                pivot -= 1

            pivot = cy
            while check_num(cx, pivot + 1, visited):
                tmp_num += schemes[cx][pivot + 1]
                pivot += 1

        if tmp_num != "":
            nums.append(int(tmp_num))

    return nums


def main(schm):
    ans = 0
    for i in range(n):
        for j in range(m):
            if schm[i][j] == "*":
                nums = get_nums(i, j)
                if len(nums) == 2:
                    ans += nums[0] * nums[1]

    return ans


print(main(schemes))
