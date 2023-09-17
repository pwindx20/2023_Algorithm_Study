# 5174
# 입력: T(1~50)/ 간선의 개수 E(1~1000), N(1~E+1)/ E개의 부모-자식 노드 번호 쌍
# 출력: #t 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
def subtree(root):
    global cnt
    if root:
        # print('root, TREE[root]:',root, TREE[root])
        cnt += 1
        subtree(TREE[root][0])
        subtree(TREE[root][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    TREE = [[0,0] for _ in range(E+2)]
    for i in range(0, 2*(E), 2):
        if TREE[edges[i]][0] != 0:
            TREE[edges[i]][1] = edges[i+1]
        else:
            TREE[edges[i]][0] = edges[i+1]
    # print('TREE:',TREE)
    
    cnt = 0
    subtree(N)
    # print('cnt:',cnt)
    print(f'#{tc} {cnt}')