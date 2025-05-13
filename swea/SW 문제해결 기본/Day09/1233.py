# 1233. [S/W 문제해결 기본] 9일차 - 사칙연산 유효성 검사
# 핵심: 계산 필요 X. 유효성만 확인!!
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    is_valid = 1  # 유효하면 1, 아니면 0

    for i in range(1, n + 1):
        line = input().split()
        idx = int(line[0])
        value = line[1]

        # 자식 노드 개수
        num_children = len(line) - 2

        if value.isdigit():
            # 숫자 노드는 자식이 없어야 함
            if num_children != 0:
                is_valid = 0
        else:
            # 연산자 노드는 반드시 자식이 2개 있어야 함
            if num_children != 2:
                is_valid = 0

    print(f"#{test_case} {is_valid}")
