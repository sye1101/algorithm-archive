# 3282. 0/1 Knapsack
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    objects = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0] * (K + 1) # dp[w] = 무게 w일 때 얻을 수 있는 최대 가치

    for weight, value in objects:
        # 무게를 역순으로 순회해야 중복 선택을 방지할 수 있음
        for w in range(K, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    print(f"#{tc} {dp[K]}")