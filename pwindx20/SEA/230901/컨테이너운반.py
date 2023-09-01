# 5201
# 입력: T/ 컨테이너 수 N, 트럭 수 M/ 화물의 무게 wi/ 트럭의 적재용량 ti
# 출력: #t 옮겨진 화물의 전체 무게
# 트럭당 한개의 컨테이너만 운반가능 적재용량 초과 컨테이너 운반불가
# 컨테이너를 한개도 옮길수 없는 경우 0 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    W_lst = sorted(list(map(int,input().split())), reverse=True)
    T_lst = sorted(list(map(int,input().split())), reverse=True)
    total = 0
    while W_lst and T_lst: # 뒤의 조건을 안써서 틀림 !! 
        if T_lst[0] >= W_lst[0]:
            T_lst.pop(0)
            total += W_lst[0]
        W_lst.pop(0)
     
    print(f'#{tc} {total}')