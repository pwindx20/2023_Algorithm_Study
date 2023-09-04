# 2817
# 입력: T/ N(1~20) K(1~1000)/ N개의 자연수 수열 A (1~100, 공백 O)
# 출력: #tc 부분수열의 합이 K가 되는 경우의 수를 출력
def subset(k, sumV):
    global cnt
    # if sub in memo:
    #     return
    
    if k == N:
        # print(bits)
        if sumV == K:
            cnt += 1
        return
    
    bits[k] = 0
    subset(k+1, sumV)
    bits[k] = 1
    subset(k+1, sumV + A[k])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    bits = [0]* N
    subset(0, 0)
    print(f'#{tc} {cnt}')
    
    
    # 메모이제이션이나 백트래킹? 을 쓰고 싶었는데
    # 방법을 모르겠음
    # 다음에 강의영상보면서 다시 확인해봐야겠다.