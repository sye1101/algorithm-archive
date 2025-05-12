# 1204. [S/W 문제해결 기본] Day01 - 최빈수 구하기
from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    grades = list(map(int, input().split())) # 점수
    count = Counter(grades)

    mode = max(count.items(), key=lambda x: (x[1], x[0]))[0]

    print(f"#{test_case} {mode}")