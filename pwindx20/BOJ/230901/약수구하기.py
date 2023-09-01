# 2501
# 입력: N (1~10,000), K (1~N)
# 출력: N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K보다 적어서 존재하지 않을경우 0

N, K = map(int, input().split())
for i in range(1, N+1): # N+1을 안해서 틀렸음
    if N % i == 0:
        K-=1
        if K == 0:
            print(i)
            break
else:
    print(0)