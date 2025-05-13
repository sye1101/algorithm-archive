# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
T = 10
for test_case in range(1, T + 1):
    n, data = input().split()
    result = []

    for i in data:
        if not result or result[-1] != i:
            result.append(i)
        else:
            result.pop()

    print(f"#{test_case} ", *result, sep='')