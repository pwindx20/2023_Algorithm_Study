N = int(input())
perm = list(map(int, input().split()))
sorted_perm = sorted(perm)
if perm == sorted_perm:
    print(-1)