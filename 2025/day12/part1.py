#!/usr/bin/env python3
import sys


def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    shapes, regions, i = {}, [], 0

    while i < len(lines) and ":" in lines[i]:
        if "x" in lines[i]:
            break
        sid = int(lines[i].split(":")[0])
        i += 1
        slines = []
        while i < len(lines) and lines[i] and lines[i][0] in ".#":
            slines.append(lines[i])
            i += 1
        shapes[sid] = slines

    while i < len(lines):
        if "x" in lines[i] and ":" in lines[i]:
            parts = lines[i].split(":")
            w, h = map(int, parts[0].split("x"))
            counts = list(map(int, parts[1].split()))
            regions.append((w, h, counts))
        i += 1

    return shapes, regions


def get_cells(slines):
    return [
        (r, c)
        for r, line in enumerate(slines)
        for c, ch in enumerate(line)
        if ch == "#"
    ]


def normalize(cells):
    if not cells:
        return []
    mr, mc = min(r for r, c in cells), min(c for r, c in cells)
    return [(r - mr, c - mc) for r, c in cells]


def get_variants(cells):
    vs = set()
    for flip in [False, True]:
        cur = cells[:]
        if flip:
            cur = [(r, -c) for r, c in cur]
        for _ in range(4):
            vs.add(tuple(sorted(normalize(cur))))
            cur = [(c, -r) for r, c in cur]
    return [list(v) for v in vs]


def can_place(grid, shape, r, c):
    h, w = len(grid), len(grid[0])
    for dr, dc in shape:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w or grid[nr][nc]:
            return False
    return True


def place(grid, shape, r, c, mark):
    for dr, dc in shape:
        grid[r + dr][c + dc] = mark


def unplace(grid, shape, r, c):
    for dr, dc in shape:
        grid[r + dr][c + dc] = 0


def backtrack(grid, pieces, variants, idx):
    if idx >= len(pieces):
        return True

    h, w = len(grid), len(grid[0])
    sid = pieces[idx]

    # Try all positions and all variants
    for r in range(h):
        for c in range(w):
            for var in variants[sid]:
                if can_place(grid, var, r, c):
                    place(grid, var, r, c, idx + 1)
                    if backtrack(grid, pieces, variants, idx + 1):
                        return True
                    unplace(grid, var, r, c)

    return False


def solve(w, h, shapes, counts):
    variants, sizes = {}, {}
    for sid, sdef in shapes.items():
        cells = get_cells(sdef)
        variants[sid] = get_variants(cells)
        sizes[sid] = len(cells)

    pieces = []
    for sid, cnt in enumerate(counts):
        pieces.extend([sid] * cnt)

    if sum(sizes.get(p, 0) for p in pieces) > w * h:
        return False

    pieces.sort(key=lambda p: sizes.get(p, 0), reverse=True)

    grid = [[0] * w for _ in range(h)]
    return backtrack(grid, pieces, variants, 0)


def main():
    shapes, regions = parse_input("2025/day12/input.txt")

    print(f"Shapes: {len(shapes)}, Regions: {len(regions)}")
    print("=" * 60)

    ans = 0
    for i, (w, h, counts) in enumerate(regions, 1):
        tot = sum(counts)
        print(
            f"{i:3}/{len(regions)}: {w:2}x{h:2} ({tot:3} pcs) ...", end=" ", flush=True
        )
        if solve(w, h, shapes, counts):
            print("YES")
            ans += 1
        else:
            print("NO")

    print("=" * 60)
    print(f"Answer: {ans}")


if __name__ == "__main__":
    main()
