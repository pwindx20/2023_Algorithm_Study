N = int(input())

candy = [list(input()) for _ in range(N)]

candy_c = candy
candy_p = candy
candy_y = candy
candy_z = candy
# print(candy)

#색깔은 C, P, Y, Z

for i in range(N):
    for j in range(N):
        for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
            ni = i + di
            nj = j + dj
            if candy[i][j] == 'C' and 0 <= ni < N and 0 <= nj <N:
                candy_c[ni][nj] = 'C'

for i in range(N):
    for j in range(N):
        for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
            ni = i + di
            nj = j + dj
            if candy[i][j] == 'P' and 0 <= ni < N and 0 <= nj <N:
                candy_p[ni][nj] = 'P'

for i in range(N):
    for j in range(N):
        for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
            ni = i + di
            nj = j + dj
            if candy[i][j] == 'Y' and 0 <= ni < N and 0 <= nj <N:
                candy_y[ni][nj] = 'Y'

for i in range(N):
    for j in range(N):
        for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
            ni = i + di
            nj = j + dj
            if candy[i][j] == 'Z' and 0 <= ni < N and 0 <= nj <N:
                candy_z[ni][nj] = 'Z'

max_c = 0
for i in range(N):
    cnt_c = 0
    for j in range(N):
        if candy_c[i][j] == 'C':
            cnt_c += 1
        else:
            if max_c < cnt_c:
                max_c = cnt_c
                cnt_c = 0

for j in range(N):
    cnt_c = 0
    for i in range(N):
        if candy_c[i][j] == 'C':
            cnt_c += 1
        else:
            if max_c < cnt_c:
                max_c = cnt_c
                cnt_c = 0

max_p = 0
for i in range(N):
    cnt_p = 0
    for j in range(N):
        if candy_p[i][j] == 'P':
            cnt_p += 1
        else:
            if max_p < cnt_p:
                max_p = cnt_p
                cnt_p = 0

for j in range(N):
    cnt_p = 0
    for i in range(N):
        if candy_p[i][j] == 'P':
            cnt_p += 1
        else:
            if max_p < cnt_p:
                max_p = cnt_p
                cnt_p = 0

max_y = 0
for i in range(N):
    cnt_y = 0
    for j in range(N):
        if candy_y[i][j] == 'Y':
            cnt_y += 1
        else:
            if max_y < cnt_y:
                max_y = cnt_y
                cnt_y = 0

for j in range(N):
    cnt_y = 0
    for i in range(N):
        if candy_y[i][j] == 'Y':
            cnt_y += 1
        else:
            if max_y < cnt_y:
                max_y = cnt_y
                cnt_y = 0

max_z = 0
for i in range(N):
    cnt_z = 0
    for j in range(N):
        if candy_z[i][j] == 'Z':
            cnt_z += 1
        else:
            if max_z < cnt_z:
                max_z = cnt_z
                cnt_z = 0

for j in range(N):
    cnt_z = 0
    for i in range(N):
        if candy_z[i][j] == 'Z':
            cnt_z += 1
        else:
            if max_z < cnt_z:
                max_z = cnt_z
                cnt_z = 0

lst = [cnt_z, cnt_c, cnt_p, cnt_y]
print(cnt_z, cnt_c, cnt_p, cnt_y)
print(candy_c)
print(max(lst))

#문제 잘못 읽어서 시간 버림
#한칸씩 색깔 바꿀 때 마다 갯수 어케 세나요
