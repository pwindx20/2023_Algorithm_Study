def room(num):
    global cnt
    if num >= K:
        cnt += num//2
        cnt += num%2
    elif 0 < num < K:
        cnt += 1
    else:
        return cnt
    return cnt
    
arr = [[] for _ in range(7)]
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    arr[Y].append(S)
# print(arr)
cnt = 0
for i in range(1,7):
    room(arr[i].count(0))
    room(arr[i].count(1))
print(cnt)