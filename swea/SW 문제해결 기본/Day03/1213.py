# 1213. [S/W 문제해결 기본] Day03 - String
T = 10
for test_case in range(1, T + 1):
    _ = input()
    target = input()
    sentence = input()

    result = sentence.count(target)

    print(f"#{test_case} {result}")

"""
# 내가 쓴 코드
T = 10
def find(start, target, sentence):
    length = len(target)
    idx = 0
    for i in range(start, start + length):
        if sentence[i] == target[idx]:
            idx += 1
            continue
        else:
            return False
    return True

for test_case in range(1, T + 1):
    _ = input()
    target = input() # 타겟 문자열
    sentence = input()

    result = 0
    for i in range(0, len(sentence) - len(target) + 1):
        if not find(i, target, sentence):
            continue
        else:
            result += 1

    print(f"#{test_case} {result}")
"""