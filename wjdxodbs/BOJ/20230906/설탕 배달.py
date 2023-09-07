from sys import stdin
input = stdin.readline

N = int(input())
for i in range(N//5, -1, -1):
    a = N - 5 * i
    if a % 3 == 0:
        print(i+a//3)
        break
else:
    print(-1)