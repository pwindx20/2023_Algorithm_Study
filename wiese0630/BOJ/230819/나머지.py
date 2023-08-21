lst = []
for _ in range(10):
    lst += [int(input())]

ansset = set()

for elem in lst:
    ansset.add(elem%42)
print(len(ansset))