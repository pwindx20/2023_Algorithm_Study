# 15650
# 입력: N, M
# 출력: 중복없이 M개를 고른 수열, 오름차순
def per(k, M):
    if k == M:
        print(*result)
        return
    for i in range(1,N+1):
        if not used[i]:
            result[k] = i
            used[i] = True
            per(k+1, M)
        used[i] = False
            
N, M = map(int,input().split())
used = [True]+[False]*(N)
result = [-1]*M
per(0, M)