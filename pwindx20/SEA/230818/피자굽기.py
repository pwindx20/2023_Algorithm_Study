# 5099
# 입력: 테스트케이스 개수 T/ 화덕크기 N (3~20) 피자개수 M (N~100)/ Ci
# 출력: #t 가장 마지막 치즈
def pizza():
    q = list(range(1, N+1))
    i = 1
    while q:
        idx = q.pop(0)
        cheese[idx] //= 2
        if cheese[idx]==0: 
            if N+i <= M:
                q.append(N+i)
                i += 1
        else:
            q.append(idx)
        print(q)
        print(cheese)
    return idx


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))
    print(f'#{tc} {pizza()}')
    