# 5177
# 완전이진트리 부모노드값 < 자식노드
# 루트가 1번, 왼쪽에서 오른쪽으로
# 입력: T(1~50)/ N(5~500)/ 1,000,000이하인 서로다른 N개의 자연수
# 출력: #t 마지막노드의 조상노드에 저장된 정수의 합
def minheap(root):
    TREE.append(node_data[root])
    c = root
    while c//2 > 0 and TREE[c] < TREE[c//2]:
        p = c//2
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TREE = [0]
    node_data = [0]+list(map(int, input().split()))
    for i in range(1,N+1):
        minheap(i)
    # print(TREE)
    sum_p = 0
    node = N//2
    while node>0:
        sum_p += TREE[node]
        node //= 2
    print(f'#{tc} {sum_p}')