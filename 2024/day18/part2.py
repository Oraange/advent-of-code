import os
from collections import deque

# 기본 그리드 크기(테스트 입력용)
size = 7
# 초기에 고정으로 막을 벽 개수(테스트 입력용)
start = 12


def parse_data(data):
    # "x,y" 문자열을 (x, y) 좌표 리스트로 변환
    return [tuple(map(int, line.split(","))) for line in data.splitlines()]


def bfs_reachable(block_time, blocked_count):
    # blocked_count번째까지 벽이 생겼을 때 (0,0) -> (size-1,size-1) 도달 가능 여부
    if (
        block_time[0][0] <= blocked_count
        or block_time[size - 1][size - 1] <= blocked_count
    ):
        return False

    # BFS 큐 시작점 초기화
    q = deque([(0, 0)])
    visited = [[False] * size for _ in range(size)]
    visited[0][0] = True

    while q:
        cx, cy = q.popleft()
        # 도착점에 도달하면 성공
        if cx == cy == size - 1:
            return True
        for dx, dy in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < size and 0 <= ny < size and not visited[ny][nx]:
                # 해당 칸이 blocked_count 이전에 막히면 통과 불가
                if block_time[ny][nx] <= blocked_count:
                    continue
                visited[ny][nx] = True
                q.append((nx, ny))

    return False


def build_block_time(data):
    # 각 좌표가 몇 번째에 막히는지 기록하는 타임스탬프 그리드
    block_time = [[float("inf")] * size for _ in range(size)]
    for idx, (x, y) in enumerate(data):
        block_time[y][x] = idx
    return block_time


def main(data, width, limit):
    # 입력 크기에 맞춰 전역 설정 갱신
    global size, start
    size = width
    start = limit

    # 입력 파싱 및 차단 시점 테이블 생성
    data = parse_data(data)
    block_time = build_block_time(data)

    # 이진 탐색으로 "처음 막히는 벽"의 인덱스를 찾음
    low = start
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        # mid까지 막아도 도달 가능하면 더 뒤에서 막히는 것
        if bfs_reachable(block_time, mid):
            low = mid + 1
        else:
            high = mid

    # 처음으로 길이 막히는 벽 좌표 반환
    return data[low]


if __name__ == "__main__":
    # 입력 파일 로드
    with open("2024/day18/input.txt", "r") as f:
        data = f.read()

    # 파일명에 따라 테스트/실제 입력 구분
    if os.path.basename(f.name).startswith("test"):
        print(main(data, 7, 12))
    elif os.path.basename(f.name).startswith("input"):
        print(main(data, 71, 1024))
