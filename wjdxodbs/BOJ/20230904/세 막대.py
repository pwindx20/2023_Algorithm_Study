arr = sorted(list(map(int, input().split())))

if arr[2] >= arr[1] + arr[0]:
    print(2 * (arr[0] + arr[1]) - 1)
else:
    print(sum(arr))