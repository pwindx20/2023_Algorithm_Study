A, B = list(map(str, input().split()))
# print(A, B)
a = ''
b = ''
for i in A:
    a =  i + a
for i in B:
    b = i + b
print(max(a, b))
