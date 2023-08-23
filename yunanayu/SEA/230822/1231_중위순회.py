def inorder(root):
    global result
    if root <= N:
        inorder(root * 2)
        result = result + Tree[root]
        inorder(root * 2 + 1)
    return result


for tc in range(1, 11):
    N = int(input())
    Tree = [[] for _ in range(N + 1)]
    for _ in range(N):
        S = list(input().split())
        no = int(S[0])
        Tree[no] = S[1]
    # print(Tree)
    result = ''
    print(f'#{tc} {inorder(1)}')