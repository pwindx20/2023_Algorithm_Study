# 이전 순열
def per(k):
    global ans
    if k == N:
        # print(result)
        ans.append(result)
        for i in range(N):
            pos = result[i]
            print(lst[pos], end=' ')
        print()
        return


    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False




N = int(input())
lst = list(map(int, input().split()))
for i in range(len(lst)):
    lst[i] = lst[i] -1
# print(lst)
result = [-1] * N
visited = [False] * N
ans = []
per(0)
print(per(0))
# print(ans)