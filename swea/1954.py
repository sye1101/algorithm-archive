# 1954. 달팽이 숫자
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    num = 1
    x = y = 0
    dx = 0
    dy = 1
    while num <= n * n:
        graph[x][y] = num
        num += 1

        nx = x + dx
        ny = y + dy

        if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] != 0:
            dx, dy = dy, -dx # 방향 전환(우 -> 하 -> 좌 -> 상)

        x += dx
        y += dy

    print(f"#{test_case}")
    for i in range(n):
        print(*graph[i])