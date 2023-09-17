for tc in range(1, 11):
    print(f'#{tc}', end= ' ')
    N = int(input())
    ST = []
    result = ''

    # step1 후위 표기식으로 변경
    for s in input():
        if s.isdigit():
            result = result + s
        else:
            if ST:
                result = result + ST.pop()
            ST.append(s)
    while ST:
        result = result + ST.pop()
    
    # print(result)
    # step2 후위 표기식 계산
    for c in result:
        if c.isdigit():
            ST.append(int(c))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(v1+v2)
    print(ST.pop())



