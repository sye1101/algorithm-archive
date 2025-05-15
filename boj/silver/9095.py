# 1, 2, 3 더하기
T = int(input())

def dp(n):
    if n == 1: # 1
       return 1
    if n == 2: # 1 + 1, 2
        return 2
    if n == 3: # 1 + 1 + 1, 1 + 2, 2 + 1, 3
        return 4

    return dp(n - 1) + dp(n - 2) + dp(n - 3)

for tc in range(T):
    n = int(input())

    print(dp(n))