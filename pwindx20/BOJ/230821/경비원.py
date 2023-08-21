# 2564
# 입력: 블록의 가로, 세로 (~100)/ 상점의 개수(~100)/
# 상점의 위치- 1. 방향(1: 북쪽, 2: 남쪽, 3: 서쪽, 4: 동쪽) 
#             2. 북남쪽 - 왼쪽 경계로부터의 거리 (열), 동서쪽 - 위쪽 경계로부터의 거리 (행)
# 동근이의 위치 (상점과 같은 방식)
# 블록의 꼭짓점은 X
# 출력: 동근이의 위치와 각 상점 사이의 최단 거리의 합

M, N = map(int, input().split())
S = int(input())
store = [list(map(int, input().split())) for _ in range(S)]
pos = list(map(int, input().split()))
dis = 0

for d, pos_s in store:
    # 같은 방향에 있을 경우
    if d == pos[0]:
       dis += abs(pos_s - pos[1])

    # 반대 방향에 있을 경우 - 북남인 경우 / 동서인 경우
    elif (d+1)//2 == (pos[0]+1)//2:
        if (d+1) // 2 == 1:
            dis += N + min(pos[1] + pos_s, 2 * M - pos[1] - pos_s)
        else:
            dis += M + min(pos[1] + pos_s, 2 * N - pos[1] - pos_s)

    # 옆 방향에 있을 경우 - 동/서 구분 필요
    else:
        if d == 1:
            if pos[0] == 3:
                dis += pos[1] + pos_s
            else:
                dis += pos[1] + M - pos_s
        elif d == 2:
            if pos[0] == 3:
                dis += N - pos[1] + pos_s
            else:
                dis += N- pos[1] + M - pos_s
        elif d == 3:
            if pos[0] == 1:
                dis += pos_s + pos[1]
            else:
                dis += N - pos_s + pos[1]
        else:
            if pos[0] == 1:
                dis += pos_s + M - pos[1]
            else:
                dis += N - pos_s + M - pos[1]
print(dis)
