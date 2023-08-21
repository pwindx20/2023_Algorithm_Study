lst = []
for stu in range(28):
    lst += [int(input())]
# print(lst)

stulist = []
for num in range(1, 31):
    stulist += [num]
# print(stulist)

anslist = []
for elem in stulist:
    if elem not in lst:
        anslist += [elem]

[a, b] = anslist

if a > b:
    print(b)
    print(a)
else:
    print(a)
    print(b)