def cal(v1, v2, op):
    if op=='+':
        return v1 + v2
    if op=='-':
        return v2 - v1
    if op=='*':
        return v2 * v1
    if op=='/':
        return v2 // v1

T = int(input())

for test_case in range(1, T+1):
    lst = list(input().split())
    # print(lst)

    ST = []
    for e in lst:
        if e.isdigit():
            ST.append(int(e))
        elif e in ['/', '-', '+', '*']:
            if len(ST) > 1:
                v1 = ST.pop()
                v2 = ST.pop()
                newv = cal(v1, v2, e)
                ST.append(newv)
            else:
                ans = 'error'
                break
        else:
            v = ST.pop()
            ans = v
    if ST:
        ans = 'error'

    print(f'#{test_case} {ans}')