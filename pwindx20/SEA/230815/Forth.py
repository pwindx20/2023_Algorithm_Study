def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 // v2
    

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    code = input().split()
    ST = []
    print(code[:-1])
    for s in code[:-1]:
        if s.isdigit():
            ST.append(int(s))
        elif len(ST)>=2:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1,v2,s))
        else:
            print('error')
            break
    else: # ST의 길이가 1인 경우를 세지 않았더니 1가지 testcase에서 오답이 떴다...
        if len(ST)==1:
            print(ST.pop())
        else: 
            print('error')