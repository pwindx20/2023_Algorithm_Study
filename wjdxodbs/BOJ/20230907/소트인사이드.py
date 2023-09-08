arr = list(map(int, input()))
st = [0] * 10
result = ''
for i in arr:
    st[i] += 1
for i in range(-1, -11, -1):
    for j in range(st[i]):
        result += str(10+i)
print(result)