# 1206. [S/W 문제해결 기본] Day01 - View
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    apart = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2):
        max_left = max(apart[i-1], apart[i-2])
        max_right = max(apart[i+1], apart[i+2])
        max_value = max(max_left, max_right)
        if apart[i] > max_value:
            result += apart[i] - max_value

    print(f"#{test_case} {result}")