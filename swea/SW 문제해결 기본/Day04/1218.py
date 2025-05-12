# 1218. [S/W 문제해결 기본] Day04 - 괄호 짝짓기
# 1 - 유효함, 0 - 유효하지 않음
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    data = list(input().strip())

    stack = []
    bracket_map = {')': '(', ']': '[', '}':'{', '>':'<'}

    result = 1
    for ch in data:
        if ch in '([{<':
            stack.append(ch)
        elif ch in ')]}>':
            if not stack or stack[-1] != bracket_map[ch]:
                result = 0
                break
            stack.pop()

    print(f"#{test_case} {result}")