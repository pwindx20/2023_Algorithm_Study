# 10811
# 입력: 바구니의 개수 N, 섞는 수 M/ M개의 줄에 i, j i번째 바구니부터 j번째 바구니까지 순서를 역순으로
# 출력: 바구니에 적혀있는 순서를 출력
N, M = map(int,input().split())
basket = list(range(N+1))
for _ in range(M):
    i, j = map(int,input().split())
    basket = basket[:i]+basket[j:i-1:-1]+basket[j+1:]
    
print(' '.join(map(str, basket[1:])))