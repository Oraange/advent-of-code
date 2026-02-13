def main(disk_map: str):
    ans = 0
    block_map = []
    for i, disk in enumerate(disk_map):
        if i % 2 == 0:
            block_map.append({"id": i // 2, "size": int(disk)})
        else:
            block_map.append({"id": None, "size": int(disk)})

    r = len(block_map) - 1
    cache = {}

    while True:
        while block_map[r]["id"] is None:
            r -= 1

        if r == 0:
            break

        space = block_map[r]["size"]
        l = cache.get(space, 0)

        while (block_map[l]["id"] != None or block_map[l]["size"] < space) and l < r:
            l += 1

        cache[space] = l

        if l >= r:
            r -= 1
            continue

        move = block_map.pop(r)
        block_map.insert(r, {"id": None, "size": move["size"]})
        r -= 1

        block_map[l]["size"] -= space
        if block_map[l]["size"] == 0:
            block_map[l] = move
        else:
            block_map.insert(l, move)
            r += 1

    pos = 0
    for block in block_map:
        for _ in range(block["size"]):
            if block["id"] is not None:
                ans += block["id"] * pos
            pos += 1

    return ans


if __name__ == "__main__":
    with open("2024/day09/test.txt", "r") as f:
        disk_map = f.read().strip()
    print(main(disk_map))
