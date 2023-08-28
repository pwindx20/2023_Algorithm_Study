# def room(num):
#     global cnt
#     if num % K == 0:
#         cnt += num//2
#     elif 0 < num < K:
#         cnt += 1
#     elif num > K:
#         cnt += num//K + 1
#     else:
#         return cnt
#     return cnt

def room(num):
    global cnt
    if num % K == 0:
        cnt += num//2
    elif num != 0 :
        cnt += (num//K + 1)
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
    if len(arr[i]) != 0:
        room(arr[i].count(0))
        room(arr[i].count(1))
print(cnt)