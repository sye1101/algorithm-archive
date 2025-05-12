# 1223. [S/W 문제해결 기본] Day06 - 계산기2
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    data = list(input())
    postfix = ''
    stack = []

    priority = {'+': 1, '*': 2}

    for ch in data:
        if ch.isdigit():
            postfix += ch
        elif ch in '+*':
            while stack and priority[stack[-1]] >= priority[ch]:
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()

    cal_stack = []
    for x in postfix:
        if x.isdigit():
            cal_stack.append(int(x))
        else:
            a = cal_stack.pop()
            b = cal_stack.pop()
            if x == '+':
                cal_stack.append(a + b)
            elif x == '*':
                cal_stack.append(a * b)

    result = cal_stack[0]

    print(f"#{test_case} {result}")