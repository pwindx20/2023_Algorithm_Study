N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
# print(info)
info.sort(key=lambda x:(x[1],x[0]))
# print(info)
start = 0
cnt = 1
for i in range(1,N):
    if info[start][1] <= info[i][0]:
        cnt += 1
        start = i
print(cnt)