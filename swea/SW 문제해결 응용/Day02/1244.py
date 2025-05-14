# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
T = int(input())

def dfs(data, count):
    global result
    if count == 0:
        result = max(result, int(''.join(data)))
        return

    # 중복 방지
    key = (''.join(data), count) # (숫자상태, 남은횟수) 조합
    if key in visited:
        return
    visited.add(key)

    # 가능한 모든 위치 쌍에 대해 swap 실행
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            data[i], data[j] = data[j], data[i]
            dfs(data, count - 1)
            data[i], data[j] = data[j], data[i] # 백트래킹


for test_case in range(1, T + 1):
    data, swap = input().split()
    swap = int(swap)
    data = list(data)
    visited = set()
    result = 0

    dfs(data, swap)


    print(f"#{test_case} {result}")