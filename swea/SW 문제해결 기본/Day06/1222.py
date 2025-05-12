# 1222. [S/W 문제해결 기본] Day06 - 계산기1
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    data = list(input())
    stack = []
    postfix = ''
    result = 0

    # 중위표기식 -> 후위표기식
    for ch in data:
        if ch.isdigit():
            postfix += ch
        elif ch == '+':
            while stack:
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    cal_stack = []
    for x in postfix:
        if x.isdigit():
            cal_stack.append(int(x))
        else:
            a = cal_stack.pop()
            b = cal_stack.pop()
            cal_stack.append(a + b)

    result = cal_stack[0]

    print(f"#{test_case} {result}")