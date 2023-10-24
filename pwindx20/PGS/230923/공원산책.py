# 입력: 공원 정보/ 명령
# 출력: 위치
def solution(park, routes):
    H, W = len(park),len(park[0])
    isF = 0
    for i in range(H):
        for j in range(W):
            if park[i][j]=='S':
                x, y = i, j
                isF = 1     
                break
        if isF:
            break
    
    for order in routes:
        op, n = order.split()
        n = int(n)
        if op == 'N':
            di, dj = -1, 0
        elif op == 'S':
            di, dj = 1, 0
        elif op =='W':
            di, dj = 0, -1
        else:
            di, dj = 0, 1
        
        nx = x+di*n
        ny = y+dj*n

        if 0> nx or H<= nx or 0> ny or W<=ny:
            continue        

        else:
            for k in range(1,n+1):
                if park[x+di*k][y+dj*k] =='X':
                    break
            else:
                x = nx
                y = ny
    return [x, y]
