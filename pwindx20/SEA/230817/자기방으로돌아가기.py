# 4408 
# 입력: T/ 학생수 N / 현재방, 돌아갈방 <=400 중복X
# 출력: #t 전부 돌아가는 데 걸리는 시간

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0]*201
    for _ in range(N):
        s, e = sorted(list(map(int, input().split())))
        for i in range((s+1)//2, (e+1)//2+1):
            corridor[i] += 1
    print(f'#{tc} {max(corridor)}')