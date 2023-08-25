# 1220 
# 테이블 앞, 뒤쪽 N, S에만 반응 자성체끼리는 반응X 10개의 테스트케이스 위쪽이 N, 아래쪽이 S
# 입력: 정사각형의 한변의 길이 100/ 1:N극, 2: S극
# 출력: 교착상태

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        temp = []
        for i in range(N):
            if table[i][j] != 0:
                temp.append(table[i][j])
        while temp:
            if temp[0] == 2:
                temp.pop(0)
                continue
            if temp[-1] == 1:
                temp.pop()
                continue
            break
        ns = ''.join(map(str,temp))
        cnt += ns.count('12')
        
    print(f'#{tc} {cnt}')