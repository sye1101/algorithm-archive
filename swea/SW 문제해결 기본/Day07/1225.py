# 1225. [S/W 문제해결 기본] Day07 - 암호생성기
T = 10
for test_case in range(1, T + 1):
    _ = input()
    q = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        tmp = q.pop(0) - i
        if tmp > 0:
            q.append(tmp)
        else: # 0보타 작거나 같으면 종료
            tmp = 0
            q.append(tmp)
            break
        i += 1

    print(f'#{test_case}', *q)