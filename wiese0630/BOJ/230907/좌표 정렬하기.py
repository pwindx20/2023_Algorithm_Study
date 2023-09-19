N = int(input())

lst_x = []
lst_y = []

for _ in range(N):
    X, Y = map(int, input().split())
    lst_x.append(X)
    lst_y.append(Y)


print(lst_x)
print(lst_y)

# for i in range(N):
#     print(lst_x[i], lst_y[i])