T = 10

def STEP1(s):
    result = []
    ST = []
    icp = {'(':3, '+':1, '-':1, '*':2, '/':2}
    isp = {'(':0, '+':1, '-':1, '*':2, '/':2}
    for c in s:
        if c.isdigit():
            result.append(c)
        # elif c == '(':
        elif c == ')':
            while ST and ST[-1] != '(':
                v = ST.pop()
                result.append(v)
            ST.pop()        # ( 버림
        else:
            while ST and isp[ST[-1]] >= icp[c]:
                v = ST.pop()
                result.append(v)
            ST.append(c)

    while ST:
        v = ST.pop()
        result.append(v)
    return result

def cal(v1, v2, op):
    if op=='+':
        return v1 + v2
    if op=='*':
        return v2 * v1

def STEP2(s):
    ST = []
    for c in s:
        if c.isdigit():
            ST.append(c)
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(cal(int(v1), int(v2), c))
    return ST.pop()

for test_case in range(1, T+1):
    N = int(input())
    str = input()
    rst1 = STEP1(str)
    # print(rst1)
    rst2 = STEP2(rst1)
    print(f'#{test_case} {rst2}')
