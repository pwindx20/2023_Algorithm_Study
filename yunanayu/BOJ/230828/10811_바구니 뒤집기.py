N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
    basket.append(i)
for _ in range(M):
    i, j = map(int, input().split())
    lst = basket[i-1:j:][::-1]
    m = 0
    for k in range(i-1,j):
        basket[k-1] = lst[m]
        m+=1
    # print(basket)
    # basket[i:i+j] = lst
#     # print(lst)
print(*basket)
# basket[0] = 10
# print(basket)