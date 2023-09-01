# 4012
# N/2개씩 나누어 두개의 요리(N은 짝수)
# 입력: T(1~50)/ 식재료 수 N(4~16 짝수)/ 시너지 Sij (1~20,000 i!=j)
# 출력: #t 두 음식간의 맛의 차이가 최소가 되는 경우, 그 최솟값을 출력

def comb(k, s): # k: depth, s: startpoint
    if k == N//2:
        Sa = bits[:]
        Sb = list(set(range(N))-set(Sa))
        sumSa = sumSb = 0
        for j in range(N//2):
            for k in range(N//2):
                sumSa += S[Sa[j]][Sa[k]]
                sumSb += S[Sb[j]][Sb[k]]
        diff.append(abs(sumSa-sumSb))
        return
    
    for i in range(s, N//2+1+k):
        bits[k] = i
        comb(k+1, i+1)
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    bits = [-1] * (N//2)
    diff = []
    comb(0, 0)
    print(f'#{tc} {min(diff)}')
    

# 조합을 아직 이해 못함 다시 풀기!!