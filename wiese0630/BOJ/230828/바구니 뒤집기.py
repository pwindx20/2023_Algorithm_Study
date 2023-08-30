N, M = map(int, input().split())
basket = [0]
for i in range(1, N+1):
    basket.append(str(i))
# print(basket)
# 바구니 기본형 만들기

for _ in range(M):
    i, j = map(int, input().split())
    ans = basket[:i] + basket[j:i-1:-1] + basket[j+1:]
    basket = ans
#슬라이싱해서 거꾸로 만들기

ans.pop(0)
# 0 제거하기

ans_str = ' '.join(ans)
#join 써서 답 모양 만들기

print(ans_str)
