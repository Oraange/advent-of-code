def is_valid(pages: dict, ordering: list):
    res = 0
    for ordr in ordering:
        checked = set()
        vlid = True

        for i in range(1, len(ordr)):
            checked.add(ordr[i - 1])
            next_pages = pages.get(ordr[i])

            if not next_pages:
                continue

            if checked & next_pages:
                vlid = False
                break

        if vlid:
            res += int(ordr[len(ordr) // 2])

    return res


def parsing(lines: list):
    pages = {}
    ordering = []
    for line in lines:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if x not in pages:
                pages[x] = {y}
            else:
                pages[x].add(y)
        elif "," in line:
            ordering.append(tuple(map(int, line.split(","))))

    return pages, ordering


def main(lines: str):

    lines = lines.strip().splitlines()
    pgs, ordring = parsing(lines)
    return is_valid(pgs, ordring)


if __name__ == "__main__":
    with open("2024/day05/input.txt", "r") as f:
        lines = f.read()
    print(main(lines))
