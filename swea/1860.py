# 1860. 진기의 최고급 붕어빵
T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split()) # 사람 수, 걸리는 시간, 붕어빵 수
    waiting = list(map(int, input().split()))
    waiting.sort() # 도착 시간 순서대로 정렬

    flag = True
    for i in range(n):
        arrival = waiting[i]
        made = (arrival // m) * k # 도착 시각까지 만들어진 붕어빵 개수
        if made < (i + 1):  # 지금까지 도착한 사람 수보다 빵이 적으면
            flag = False
            break

    result = "Possible" if flag else "Impossible"
    print(f"#{test_case} {result}")