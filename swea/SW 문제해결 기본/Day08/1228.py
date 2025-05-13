# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
from collections import deque

T = 10
for test_case in range(1, T + 1):
    length = int(input()) # 원본 암호문의 길이
    origin = list(map(int, input().split())) # 원본 암호문
    n = int(input()) # 명령어의 개수
    orders = list(input().split()) # 명령어

    data = deque(orders)

    while data:
        cmd = data.popleft()
        if cmd == 'I':
            x = int(data.popleft())
            y = int(data.popleft())
            for i in range(y):
                s = int(data.popleft())
                origin.insert(x + i, s)

    result = ' '.join(map(str, origin[:10]))

    print(f"#{test_case} {result}")