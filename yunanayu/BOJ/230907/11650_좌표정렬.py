N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
# print(lst)
lst.sort()
for l in lst:
    print(*l)