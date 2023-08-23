# 1231
# 입력: 10개의 tc / 트리가 갖는 정점의 총 수 N(1~100) / 정점 정보 해당 정점의 문자, 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서
# 정점번호1~N 정점을 매기는 규칙은 완전트리 루트 정점은 항상 1
# 출력: #tc inorder형식으로 순회했을 때 나오는 단어
def in_order(root):
    
    if root != 0:
        in_order(TREE[root][1])
        print(TREE[root][0], end= '')
        in_order(TREE[root][2])

for tc in range(1, 11):
    N = int(input())
    
    #TREE 생성
    TREE = [['', 0, 0] for _ in range(N+1)]
    for _ in range(N):
        node_data = input().split()
        idx = int(node_data[0])
        TREE[idx][0] = node_data[1]
        if len(node_data) == 3:
            TREE[idx][1] = int(node_data[2])
        elif len(node_data) == 4:
            TREE[idx][1] = int(node_data[2])
            TREE[idx][2] = int(node_data[3])
    print(f'#{tc}', end=' ')
    in_order(1)
    print()