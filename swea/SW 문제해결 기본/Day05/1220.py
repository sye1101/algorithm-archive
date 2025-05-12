# 1220. [S/W 문제해결 기본] Day05 - Magnetic
# 0: 빈칸, 1: N극, 2: S극
T = 10

for test_case in range(1, T + 1):
    n = int(input()) # 100
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    for y in range(100):
        flag = False
        for x in range(100):
            if data[x][y] == 1:
                flag = True
            if flag and data[x][y] == 2:
                result += 1
                flag = False

    print(f"#{test_case} {result}")