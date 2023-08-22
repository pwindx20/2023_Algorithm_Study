def pre_order(root):
    global cnt
    if root:
        cnt += 1
        pre_order(Tree[root][0])
        pre_order(Tree[root][1])
    return cnt


TC = int(input())
for tc in range(1, TC + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    Tree = [[0, 0] for _ in range(E + 2)]
    for i in range(0, len(arr), 2):
        p = arr[i]
        c = arr[i + 1]
        if Tree[p][0] == 0:
            Tree[p][0] = c
        else:
            Tree[p][1] = c
    cnt = 0
    print(f'#{tc} {pre_order(N)}')