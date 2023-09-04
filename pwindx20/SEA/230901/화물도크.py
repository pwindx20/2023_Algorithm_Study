# 5202
# 입력: T(1~50)/ 신청서 개수 N(1~100)/ 작업시작시간 s(0<= <24) 종료시간 e (0< <=24)
# 출력: #t 최대 몇대 이용할 수 있는지 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
    
    times.sort(key=lambda x: x[1])
    # print(times)
    DOCK = []
    j = 0
    for i in range(1, N+1):
        if times[i][0] >= times[j][1]:
            DOCK.append(i)
            j = i
            
    print(f'#{tc} {len(DOCK)}')
    
    # 아직도 잘 모르겠다 한번 더 풀어봐야겠음