# 1209. [S/W 문제해결 기본] 2일차 - Sum
T = 10

for test_case in range(1, T + 1):
    _ = input()
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    for x in range(100):
        sum_x = 0
        sum_y = 0
        for y in range(100):
            sum_x += data[x][y]
            sum_y += data[y][x]
        result = max(result, sum_x, sum_y)
    
    # 좌측 대각선
    sum_z1 = 0
    for x in range(100):
        sum_z1 += data[x][x]

    # 우측 대각선
    sum_z2 = 0
    idx = 0
    for x in range(99, -1, -1):
        sum_z2 += data[idx][x]
        idx += 1

    result = max(result, sum_z1, sum_z2)

    print(f"#{test_case} {result}")