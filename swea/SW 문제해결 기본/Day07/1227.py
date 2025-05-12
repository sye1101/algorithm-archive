# 1227. [S/W 문제해결 기본] Day07 - 미로2
# 1: 벽, 2: 출발점, 3: 도착점
# 출력: 1 - 가능함, 0 - 가능하지 않음
from collections import deque

T = 10

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and data[nx][ny] != '1':
                if data[nx][ny] == '3':
                    return True
                q.append((nx, ny))
                visited[nx][ny] = True
    return False


for test_case in range(1, T + 1):
    _ = input()
    data = []
    start = None


    visited = [[False] * 100 for _ in range(100)]

    for i in range(100):
        tmp = list(input().strip())
        data.append(tmp)
        if start is None:
            for j in range(100):
                if tmp[j] == '2':
                    start = (i, j)
                    break

    if bfs(start[0], start[1]):
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")