# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
T = 10

def inorder(x):
    inorder(stack[x][0]) if len(stack[x]) > 0 else None # 왼쪽 노드 방문
    inorder(stack[x][1]) if len(stack[x]) > 1 else None # 오른쪽 노드 방문

    if dic[x].isdigit():
        dic[x] = int(dic[x])
    else:
        op = dic[x]
        left = dic[stack[x][0]]
        right = dic[stack[x][1]]

        if op == '+':
            dic[x] = left + right
        elif op == '-':
            dic[x] = left - right
        elif op == '*':
            dic[x] = left * right
        elif op == '/':
            dic[x] = left // right


for test_case in range(1, T + 1):
    n = int(input())
    stack = [[] for _ in range(n + 1)]
    dic = {}

    for _ in range(1, n + 1):
        line = input().split()
        idx = int(line[0])
        ch = line[1]
        dic[idx] = ch

        if len(line) > 2: # 연결된 정점이 있는 경우
            stack[idx].append(int(line[2])) # 왼쪽 자식
            stack[idx].append(int(line[3])) # 오른쪽 자식

    inorder(1)
    result = dic[1]

    print(f"#{test_case} {result}")