def main(lines: str):
    def dfs(cur: int, i: int):
        if i == len(nums):
            if cur == target:
                return True
            else:
                return False

        if cur > target:
            return False

        if dfs(cur + nums[i], i + 1):
            return True

        if dfs(cur * nums[i], i + 1):
            return True

        if dfs(int(str(cur) + str(nums[i])), i + 1):
            return True

    lines = lines.splitlines()
    ans = 0
    for line in lines:
        target = int(line.split()[0][:-1])
        nums = list(map(int, line.split()[1:]))
        if dfs(nums[0], 1):
            ans += target

    return ans


if __name__ == "__main__":
    with open("2024/day07/input.txt", "r") as f:
        lines = f.read().strip()
        print(main(lines))
