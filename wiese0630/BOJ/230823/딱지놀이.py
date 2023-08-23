import sys
sys.stdin = open('input14696.txt', 'r')

N = int(input())

for test_case in range(N):
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    lsta = lsta[1::]
    lstb = lstb[1::]
    # print(lsta, lstb)

    cnta = [0, 0, 0, 0, 0]
    cntb = [0, 0, 0, 0, 0]
    for elem in lsta:
        cnta[elem] += 1
    for elem in lstb:
        cntb[elem] += 1
    # print(cnta)
    # print(cntb)

    result = '0'
    if cnta[4] > cntb[4]:
        result = 'A'
    elif cnta[4] < cntb[4]:
        result = 'B'
    else:
        if cnta[3] > cntb[3]:
            result = 'A'
        elif cnta[3] < cntb[3]:
            result = 'B'
        else:
            if cnta[2] > cntb[2]:
                result = 'A'
            elif cnta[2] < cntb[2]:
                result = 'B'
            else:
                if cnta[1] > cntb[1]:
                    result = 'A'
                elif cnta[1] < cntb[1]:
                    result = 'B'
                else:
                    result = 'D'

    print(result)
