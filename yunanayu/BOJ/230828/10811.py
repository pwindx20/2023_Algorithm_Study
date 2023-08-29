N, M = map(int, input().split())
lst = []
for i in range(1, N+1):
    lst.append(i)
for _ in range(M):
    i, j = map(int, input().split())
    for k in range(i-1,j//2):
        lst[k],lst[j-k-1] = lst[j-k-1], lst[k]
        # for m in range(j-1,i-2,-1):
        #     lst[k],lst[m] = lst[m], lst[k]

print(*lst)