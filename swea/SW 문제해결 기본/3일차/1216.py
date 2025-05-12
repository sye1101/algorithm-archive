# 1216. [S/W 문제해결 기본] 3일차 - 회문2
# 문제 오류: for문 안에 있는 test_case로 출력하면 오답이고, input()으로 받은 tc로 출력해야 정답.
T = 10

def is_palindrome(s):
    return s == s[::-1]

for test_case in range(1, T + 1):
    tc = int(input())
    data = [input().strip() for _ in range(100)]
    col_data = [''.join(col) for col in zip(*data)]

    result = 1
    found = False

    for length in range(100, 3, -1): # 2까지 확인
        for i in range(100):
            for j in range(101 - length):
                if is_palindrome(data[i][j:j + length]) or is_palindrome(col_data[i][j:j + length]):
                    result = length
                    found = True
                    break
            if found:
                break
        if found:
            break

    print(f"#{tc} {result}")