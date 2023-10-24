# 11047
# 입력: N, K /N개의 줄에 동전의 가치 Ai 오름차순으로 주어진다
# 출력: K원을 만드는데 필요한 동전 개수의 최솟값

N, K = map(int, input().split())

coins = sorted([int(input()) for _ in range(N)], reverse=True)
count = 0
for coin in coins:
    if K-coin>=0:
        count += K//coin
        K %= coin

print(count)
