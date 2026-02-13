def main(map_: str):
    def anti_in_map(cur_x, cur_y, comp_x, comp_y):
        nonlocal ans
        anti_x = 2 * comp_x - cur_x
        anti_y = 2 * comp_y - cur_y

        if (0 <= anti_x < n) and (0 <= anti_y < m):
            if (anti_x, anti_y) not in antinodes:
                ans += 1
                antinodes.add((anti_x, anti_y))

    map_ = map_.splitlines()
    n = len(map_)
    m = len(map_[0])
    ans = 0

    visited = dict()
    antinodes = set()

    for i in range(n):
        for j in range(m):
            antenna = map_[i][j]
            if antenna != ".":
                if antenna not in visited:
                    visited[antenna] = {(i, j)}
                else:
                    for x, y in visited[antenna]:
                        anti_in_map(i, j, x, y)
                        anti_in_map(x, y, i, j)

                    visited[antenna].add((i, j))

    return ans


if __name__ == "__main__":
    with open("2024/day08/input.txt", "r") as f:
        lines = f.read().strip()
        print(main(lines))
