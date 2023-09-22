def solution(park, routes):
    arr = []
    l = len(park)
    for i in routes:
        a, b = i.split()
        arr.append([a, int(b)])
    for i in range(l):
        le = len(park[i])
        for j in range(le):
            if park[i][j] == 'S':
                r = i
                c = j
    for i in arr:
        if i[0] == 'E':
            if c + i[1] < le:
                for i in range(1, i[1] + 1):
                    c += 1
                    if park[r][c] == 'X':
                        c -= i
                        break
        elif i[0] == 'S':
            if r + i[1] < l:
                for i in range(1, i[1] + 1):
                    r += 1
                    if park[r][c] == 'X':
                        r -= i
                        break
        elif i[0] == 'W':
            if c - i[1] >= 0:
                for i in range(1, i[1] + 1):
                    c -= 1
                    if park[r][c] == 'X':
                        c += i
                        break
        else:
            if r - i[1] >= 0:
                for i in range(1, i[1] + 1):
                    r -= 1
                    if park[r][c] == 'X':
                        r += i
                        break

    return [r, c]