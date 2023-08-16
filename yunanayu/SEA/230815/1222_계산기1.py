for tc in range(1, 11):
    L = int(input())
    txt = list(input())

    value = []
    for t in txt:
        if t != '+':
            value.append(t)

    cur_sum = 0
    for s in value:
        cur_sum += int(s)

    print(f'#{tc}', cur_sum)