# 1697
# 입력: 수빈이의 위치 N, 동생의 위치 K
# 출력: 가장 빠른 시간
# 순간이동이면 2*X 걸으면 +-1
import sys
from collections import deque
def solve(N, K):
    Q = deque()
    Q.append((N, 0))
    visited[N] = True
    while Q:
        temp, time = Q.popleft()
        if temp ==K:
            return time
        for i in [2*temp, temp-1, temp+1]:
            if 0<=i<=100000 and not visited[i]:
                Q.append((i, time+1))
                visited[temp] = True

N, K = map(int,sys.stdin.readline().split())
visited = [False]*(100001)
print(solve(N, K))


# def solve(N, K, T):
#     global min_time
#     if min_time<T or N<0 or N>100000:
#         return
    
#     if N==K:
#         min_time = T
#         return
    
#     # if N>K:
#     solve(N-1, K, T+1)
#     # else:
#     solve(N+1, K, T+1)
#     solve(N*2, K, T+1)

# N, K = map(int,input().split())
# min_time = abs(N-K)
# solve(N, K, 0)
# print(min_time)