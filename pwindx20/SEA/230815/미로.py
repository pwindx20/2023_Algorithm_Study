# learn-course에 있는 문제는 python으로 2초 내 풀이라 pass인데
# problem box에 있는 문제는 python으로 1초 내 풀이라 fail이다.
# 아직 dfs가 낯설어서 이해가 안되는 것 같다. 다시 풀어봐야지...
# 함수 활용 + 불필요한 조건 없애기

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ST = []
    
    # 도착지점의 좌표 찾기
    # for 때문에 시간 초과가 뜨나 싶어서 while로 바꿨는데 별 소용 없는 것 같다.
    i = 0
    while i<N:
        j = 0
        while j<N:
            if arr[i][j]==3:
                ST.append(i)
                ST.append(j)
                i = j = N
            j += 1
        i += 1
    
    # 델타
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    isF = False

    while ST and not isF:
        c = ST.pop()
        r = ST.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                # 이렇게 두번 나눠서 if를 한 것 때문에 오래 걸리나??
                if arr[nr][nc] == 0:
                    ST.append(nr)
                    ST.append(nc)
                elif arr[nr][nc] == 2:
                    print(1)
                    isF = True
                    break
        arr[r][c] = 1
    if not isF:
        print(0)

