# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
T = 10
def power(num, idx):
    if idx == 1:
        return num
    else:
        return num * power(num, idx-1)

for test_case in range(1, T + 1):
    _ = input()
    num, idx = map(int, input().split())

    result = power(num, idx)

    print(f"#{test_case} {result}")