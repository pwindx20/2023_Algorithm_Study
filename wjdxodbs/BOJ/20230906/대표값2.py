from sys import stdin
input = stdin.readline

arr = [int(input()) for _ in range(5)]
c = [0] * 11
sum_n = 0
for i in arr:
    c[i//10] += 1
    sum_n += i
avg_n = sum_n // len(arr)
lst = []
for i in range(11):
    while c[i]:
        lst.append(i * 10)
        c[i] -= 1
print(*[avg_n, lst[2]], sep='\n')