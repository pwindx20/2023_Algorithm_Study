TC = int(input())
for tc in range(1, TC + 1):
    arr = [list(input()) for _ in range(5)]
    for r in range(5):
        arr[r] = arr[r] + ['.'] * (15 - len(arr[r]))
    result = ''
    for c in range(15):
        for r in range(5):
            if arr[r][c] != '.':
                result = result + arr[r][c]
    print(f'#{tc} {result}')