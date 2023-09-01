# 1244
def change(k, s):
    if k == cnt+1: # cnt +1 을 안했더니 덜 돌고 저장이 안됨..!!!!
        return
    
    if s in memo[k]:
        return
    else:
        memo[k].append(s)
    
    templst = list(s)
    for i in range(N-1):
        for j in range(i+1, N):
            templst[i], templst[j] = templst[j], templst[i]
            change(k+1, ''.join(templst))
            templst[i], templst[j] = templst[j], templst[i]
            
    
T = int(input())
for tc in range(1, T+1):
    s, cnt = input().split()
    cnt = int(cnt)
    N = len(s)
    memo = [[] for _ in range(cnt+1)]
    change(0, s)
    
    print(f'#{tc} {sorted(memo[-1])[-1]}')