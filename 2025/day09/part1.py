def main(poses: str):
    poses = poses.splitlines()
    poses = [tuple(map(int, p.split(","))) for p in poses]
    n = len(poses)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_area = max(
                max_area,
                abs((1 + poses[i][0] - poses[j][0]) * (1 + poses[i][1] - poses[j][1])),
            )

    return max_area
