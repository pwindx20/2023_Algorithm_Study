T = 9
lst = []
for test_case in range(1, 10):
    num = int(input())
    lst.append(num)

ansidx = -1
maxV = 0
for idx in range(len(lst)):
    if lst[idx] > maxV:
        maxV = lst[idx]
        ansidx = idx

print(maxV)
print(ansidx + 1)