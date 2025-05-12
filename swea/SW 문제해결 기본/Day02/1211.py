# 1211. [S/W 문제해결 기본] Day02 - Ladder2
import copy

T = 10
for test_case in range(1, T + 1):
    _ = input()
    data = [list(map(int, input().split())) for _ in range(100)]

    goal_y = [i for i, val in enumerate(data[99]) if val == 1]

    min_distance = 1e9
    result = -1 # x값
    for y in goal_y:
        distance = 1
        temp = copy.deepcopy(data)
        x = 99
        while x != 0:
            temp[x][y] = 0
            if y-1 >= 0 and temp[x][y-1] == 1:
                y -= 1
            elif y+1 <= 99 and temp[x][y+1] == 1:
                y += 1
            else:
                x -= 1
            distance += 1

        val = min(min_distance, distance)
        if val != min_distance:
            result = y
            min_distance = distance

    print(f"#{test_case} {result}")