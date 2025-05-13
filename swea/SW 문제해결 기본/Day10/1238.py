# 1238. [S/W 문제해결 기본] 10일차 - Contact
from collections import deque

T = 10

def bfs(start):
    visited = [False] * 101
    q = deque()
    visited[start] = True
    q.append((start, 0))

    max_depth = 0
    result = start

    while q:
        now, depth = q.popleft()
        if depth > max_depth:
            max_depth = depth
            result = now
        elif depth == max_depth:
            result = max(result, now)

        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, depth + 1))
    return result

for test_case in range(1, T + 1):
    n, start = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(101)]

    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i + 1])

    result = bfs(start)
    print(f"#{test_case} {result}")