import sys
input = sys.stdin.readline

def a(idx):
    if len(result) == 6:
        print(*result)
        return

    for i in range(idx, N):
        result.append(arr[i])
        a(i + 1)
        result.pop()


while True:
    arr = list(map(int, input().split()))
    if not arr[0]:
        break
    result = []
    N, *arr = arr
    a(0)
    print()