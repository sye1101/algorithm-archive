# 5643. [Professional] 키 순서
from collections import deque

T = int(input())

def bfs(node, graph):
    visited = [False] * (n + 1)
    visited[node] = True
    cnt = 0
    q = deque([node])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt

for test_case in range(1, T + 1):
    n = int(input())
    m = int(input())
    tree = [[] for _ in range(n + 1)] # a -> b a보다 b가 크다
    reverse_tree = [[] for _ in range(n + 1)] # b -> a b보다 a가 작다

    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        reverse_tree[b].append(a)

    result = 0
    for i in range(1, n + 1):
        bigger = bfs(i, tree)
        smaller = bfs(i, reverse_tree)

        if bigger + smaller == n - 1:
            result += 1

    print(f"#{test_case} {result}")