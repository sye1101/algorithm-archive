# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
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
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            # 오른쪽 괄호 만나면 왼쪽 괄호까지 pop해서 후위표기식에 추가
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() # 왼쪽 괄호도 pop해주기
        elif ch in '+*':
            while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[ch]:
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
            else:
                cal_stack.append(a * b)

    print(f"#{test_case} {cal_stack[0]}")