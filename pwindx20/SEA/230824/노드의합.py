# 5178
# 입력: T(1~50)/ 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L/ 리프코드의 번호와 1000이하의 자연수
# 출력: #tc 지정한 노드번호에 저장된 값을 출력
# 리프노드를 제외한 노드에는 자식노드에 저장된 값이 들어있다.

def ch_sum(root):
    if root<=N:
        if TREE[root]:
            return TREE[root]
        # print('2*root, 2*root+1:', 2*root, 2*root+1)
        # print(TREE)
        TREE[root] = ch_sum(2*root) +ch_sum(2*root+1)
        return TREE[root]
    
    else: return 0        

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N+1)
    for _ in range(M):
        node, data = map(int, input().split())
        TREE[node] = data
    ch_sum(L)
    print(f'#{tc} {TREE[L]}')