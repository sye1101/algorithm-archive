# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
T = 10

def inorder(x):
    # 왼쪽 자식 방문
    inorder(stack[x][0]) if len(stack[x]) > 0 else None
    # 부모 노드 방문
    result.append(dic[str(x)])
    # 오른쪽 자식 방문
    inorder(stack[x][1]) if len(stack[x]) > 1 else None

for test_case in range(1, T + 1):
    n = int(input()) # 노드 개수
    stack = [[] for _ in range(n+1)]
    result = []
    dic = {}

    for i in range(1, n + 1):
        line = input().split()
        idx = line[0]
        ch = line[1]
        dic[idx] = ch

        if len(line) > 2:  # 자식 노드가 있는 경우
            stack[i].append(int(line[2]))  # 왼쪽 자식
            if len(line) > 3:
                stack[i].append(int(line[3]))  # 오른쪽 자식

    inorder(1)
    print(f"#{test_case} ", *result, sep='')