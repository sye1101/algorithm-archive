# 1226. [S/W 문제해결 기본] 7일차 - 미로1
# 1: 벽, 2: 출발점, 3: 도착점
# 출력: 1 - 가능함, 0 - 가능하지 않음
T = 10

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and data[nx][ny] != 1:
            if data[nx][ny] == 3:
                return True
            if dfs(nx, ny):
                return True
    return False

for test_case in range(1, T + 1):
    _ = input()
    data = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    start = [(i, j) for i in range(16) for j in range(16) if data[i][j] == 2]

    if dfs(start[0][0], start[0][1]):
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")