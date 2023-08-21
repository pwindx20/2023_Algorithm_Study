N = int(input())
lst = map(int, input().split())
minV = 1000000
maxV = -1000000
for elem in lst:
    if elem > maxV:
        maxV = elem
    if elem < minV:
        minV = elem
print(minV, maxV)

