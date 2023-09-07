from sys import stdin
input = stdin.readline

arr = sorted([int(input()) for _ in range(3)])
sum_n = sum(arr)
b = [0] * 3
result = ['Scalene', 'Isosceles', 'Equilateral']
for i in range(1, 3):
    if arr[i] == arr[i-1]:
        b[i] = b[i-1] + 1
if sum_n == 180:
    max_n = max(b)
    print(result[max_n])
else:
    print('Error')
    