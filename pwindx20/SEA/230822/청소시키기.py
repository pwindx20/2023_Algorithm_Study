# 16438
# 입력: T/ 거실의 크기 행 N, 열 M, 명령 수 K, 현재 행위치 R, 열위치 C/
#   M줄에 거쳐 거실의 먼지량/
#   K줄에 거쳐 명령 입력 - 방향(상:0, 하:1, 좌:2, 우:3), 이동거리
# 출력: #tc 먼지 흡입량, 최종위치 행, 열

T = int(input())
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for tc in range(1, T+1):
    N, M, K, R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dust = arr[R][C]
    arr[R][C] = 0 # 이걸 추가 안해서 계속 fail이 뜸... 초기 조건을 잘 맞춰놨는지 확인하자!
    
    for _ in range(K):
        D, S = map(int, input().split())
    
        for _ in range(S): # S번 반복
            # print('R, C:',R, C)
            nR, nC = R + direction[D][0], C + direction[D][1]
    
            if not(0 <= nR < N) or not(0 <= nC < M):
                D = 2 * (D // 2) + (D + 1) % 2
                nR, nC = R + direction[D][0], C + direction[D][1]
    
            dust += arr[nR][nC]
            arr[nR][nC] = 0
            R = nR
            C = nC
    
    print(f'#{tc}', dust, R, C)