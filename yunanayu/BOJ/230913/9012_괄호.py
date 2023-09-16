N = int(input())
for _ in range(N):
    lst = list(input())
    # print(lst)
    ST = []
    for l in lst:
        if l == '(':
            ST.append(l)
        else:
            if ST:
                if ST[-1] == '(':
                    ST.pop()
            else:
                ST.append(l)
    if ST:
        print('NO')
    else:
        print('YES')