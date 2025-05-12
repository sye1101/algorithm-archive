# 1208. [S/W 문제해결 기본] 1일차 - Flatten
T = 10

for test_case in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))

    cnt = 0
    box.sort()
    while cnt < dump:
        box[0] += 1
        box[-1] -= 1
        cnt += 1
        box.sort()

    result = box[-1] - box[0]

    print(f"#{test_case} {result}")