# 5215. 햄버거 다이어트
T = int(input())

def dfs(idx, score, cal):
    global max_score
    if cal > L:
        return
    if idx == N:
        if score > max_score:
            max_score = score
        return

    # 현재 재료를 선택하는 경우
    dfs(idx + 1, score + ingredients[idx][0], cal + ingredients[idx][1])

    # 현재 재료를 선택하지 않는 경우
    dfs(idx + 1, score, cal)

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]

    max_score = 0
    dfs(0, 0, 0)

    print(f"#{test_case} {max_score}")