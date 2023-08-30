S = input()

lst = []
for num in range(97, 123):
    idx = S.find(chr(num))
    lst.append(str(idx))

print(' '.join(lst))