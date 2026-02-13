def main(disk_map: str):
    ans = 0
    block_map = []
    for i, disk in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(disk)):
                block_map.append(str(i // 2))
        else:
            for _ in range(int(disk)):
                block_map.append(".")

    l, r = 0, len(block_map) - 1

    while l <= r:
        while block_map[l] != ".":
            l += 1
        while block_map[r] == ".":
            r -= 1

        if l >= r:
            break
        block_map[l], block_map[r] = block_map[r], block_map[l]

    for idx, num in enumerate(block_map):
        if num != ".":
            ans += idx * int(num)

    return ans


if __name__ == "__main__":
    with open("2024/day09/input.txt", "r") as f:
        disk = f.read().strip()
        print(main(disk))
