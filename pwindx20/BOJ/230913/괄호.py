# 9012
# 입력: T / 괄호 문자열
# 출력: 'YES' or 'NO'

T = int(input())
for i in range(T):
    ps = input()
    ST = []
    for s in ps:
        if s =='(':
            ST.append(s)
        elif s ==')' and ST:
            v = ST.pop()
            if v !='(':
               print('NO')
               break
        else: 
            print('NO')
            break
    else:
        if ST:
            print('NO')
        else:
            print('YES') 