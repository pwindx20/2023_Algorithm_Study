lst_X = []
lst_Y = []

for _ in range(3):
    X, Y = map(int, input().split())
    lst_X.append(X)
    lst_Y.append(Y)

for elem in lst_X:
    if lst_X.count(elem) == 1:
        ansX = elem

for elem in lst_Y:
    if lst_Y.count(elem) == 1:
        ansY = elem

print(ansX, ansY)