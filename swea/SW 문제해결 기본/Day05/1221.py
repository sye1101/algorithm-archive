# 1221. [S/W 문제해결 기본] Day05 - GNS
T = int(input())

for test_case in range(1, T + 1):
    tc_line = input().split()
    tc, n = tc_line[0], int(tc_line[1])

    data = list(input().split())

    num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    data.sort(key=lambda x:num_dic[x])
    print(tc)
    print(*data)