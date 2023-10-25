from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    total = 0
    save = arr[l-1]
    for i in range(l-2, -1, -1):
        if save >= arr[i]:
            total += (save-arr[i])
        else:
            save = arr[i]

    print(total)