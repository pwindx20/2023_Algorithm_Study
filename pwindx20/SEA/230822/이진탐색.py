# 5176
# 입력: T (1~50)/ N(1~1000)
# 출력: #t 완전 이진트리로 만든 이진 탐색 트리의 루트에 저장된 값과 N/2번 노드에 입력된 값을 출력
def in_order(root):
    
    global value # 전혀 기억나지 않아서 슬쩍 봤습니다...
    
    if root <= N:
        in_order(root*2)
        TREE[root] = value
        value += 1
        in_order(root*2+1)
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    value = 1
    in_order(1)
    print(f'#{tc} {TREE[1]} {TREE[N//2]}')