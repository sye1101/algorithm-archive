# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
T = 10

def dfs(data, start, visited):
    if start == 99:
        return True
    visited[start] = True
    for i in data[start]:
        if not visited[i]:
            if dfs(data, i, visited):
                return True
    return False

for test_case in range(1, T + 1):
    tc, n = map(int, input().split())
    raw = list(map(int, input().split()))
    data = [[] for _ in range(100)]

    for i in range(0, len(raw), 2):
        data[raw[i]].append(raw[i+1])

    visited = [False] * 100
    result = dfs(data, 0 ,visited)

    if result:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")