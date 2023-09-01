# 4408
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cor = [0] *201
    for _ in range(N):
        a, b = map(int, input().split())
        if a>b: a, b= b, a
        for i in range((a+1)//2, (b+1)//2+1):
            cor[i] += 1
    print(f'#{tc} {max(cor)}')