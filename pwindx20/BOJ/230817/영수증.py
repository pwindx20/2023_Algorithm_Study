# 25304
# 입력: 총금액/ 물건의 종류 수 / 가격a, 개수 b
# 출력: 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증의 총금액과 일치하면 Yes , 아니면 No

X=int(input())
N = int(input())
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a*b
print('Yes') if total == X else print('No')