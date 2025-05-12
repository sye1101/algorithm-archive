# 1215. [S/W 문제해결 기본] Day03 - 회문1
T = 10
def is_palindrome(s):
    return s == s[::-1]

for test_case in range(1, T + 1):
    length = int(input())
    data = [input().strip() for _ in range(8)]
    result = 0

    col_data = list(zip(*data))

    # 가로 확인
    for row in data:
        for i in range(8 - length + 1):
            substring = row[i:i + length]
            if is_palindrome(substring):
                result += 1

    # 세로 확인
    for col in col_data:
        for i in range(8 - length + 1):
            substring = col[i:i + length]
            if is_palindrome(substring):
                result += 1

    print(f"#{test_case} {result}")


"""
T = 10

def is_palindrome(s):
    return s == s[::-1]

for test_case in range(1, T + 1):
    length = int(input())
    data = [input().strip() for _ in range(8)]
    result = 0

    # 가로 확인
    for row in data:
        for i in range(8 - length + 1):
            substring = row[i:i+length]
            if is_palindrome(substring):
                result += 1

    # 세로 확인
    for col in range(8):
        for i in range(8 - length + 1):
            substring = ''.join([data[j][col] for j in range(i, i+length)])
            if is_palindrome(substring):
                result += 1

    print(f"#{test_case} {result}")
"""