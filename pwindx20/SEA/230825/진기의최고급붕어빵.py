# 1860
# 입력: T/ N, M, K (~100)/ N개의 정수 (초단위 ~11,111)
# 출력: #tc Possible/Impossible

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    item = 0
    for i in range(len(people)):
        item = K*(people[i]//M) -i-1
        # print('item:',item)
        if item<0:
            print('Impossible')
            break
    else:
        print('Possible')