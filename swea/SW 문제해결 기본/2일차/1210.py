# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# 문제의 x를 코드에서는 y로 표기
T = 10

for test_case in range(1, T + 1):
    _ = input()

    data = [list(map(int, input().split())) for _ in range(100)]

    x = 99
    y = data[99].index(2)

    while x != 0:
        data[x][y] = 0  # 방문 표시
        if y - 1 >= 0 and data[x][y-1] == 1: # 왼쪽 검사
            y -= 1
        elif y + 1 <= 99 and data[x][y+1] == 1: # 오른쪽 검사
            y += 1
        else:
            x -= 1

    print(f"#{test_case} {y}")