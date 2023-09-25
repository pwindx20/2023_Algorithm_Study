# N과 M(1)
# 입력: N, M
# 출력: 사전순으로 출력
def solve(k):
    
    if k == M:
        print(*result)
        return
    for i in range(k+1,N-(M-k)+2):
        if not used[i]:
           result[k] = i
           used[i] = True 
           solve(k+1)
           used[i] = False
            
N, M = map(int,input().split())
used = [True]+[False]*N
result = [0]*M
solve(0)