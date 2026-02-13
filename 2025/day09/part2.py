from itertools import combinations


def cal_area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def build_edges(poses: list[tuple[int, int]]):
    edges = []
    n = len(poses)
    for i in range(n):
        edges.append(
            (
                min(poses[i][0], poses[(i + 1) % n][0]),
                min(poses[i][1], poses[(i + 1) % n][1]),
                max(poses[i][0], poses[(i + 1) % n][0]),
                max(poses[i][1], poses[(i + 1) % n][1]),
            )
        )

    return edges


def is_contained(mn_x, mn_y, mx_x, mx_y, edges):
    for e_mn_x, e_mn_y, e_mx_x, e_mx_y in edges:
        if mn_x < e_mx_x and mx_x > e_mn_x and mn_y < e_mx_y and mx_y > e_mn_y:
            return False

    return True


def main2(poses: str):
    poses = poses.splitlines()
    poses = [tuple(map(int, p.split(","))) for p in poses]
    edges = build_edges(poses)

    ans = 0

    for a, b in combinations(poses, 2):
        area = cal_area(a, b)

        if area <= ans:
            continue

        if is_contained(
            min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1]), edges
        ):
            ans = area

    return ans


if __name__ == "__main__":
    with open("2025/day9/input.txt", "r", encoding="utf-8") as f:
        poses = f.read().strip()
    print(main2(poses))
