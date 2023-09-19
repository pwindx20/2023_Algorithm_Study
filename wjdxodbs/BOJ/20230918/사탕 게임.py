from sys import stdin
input = stdin.readline

def a():
    max_n = 0
    for i in range(N):
        d = max(b(arr[i]), b(arr_n[i]))
        if max_n == N:
            return max_n
        elif max_n < d:
            max_n = d

    for i in range(N):
        for j in range(1, N):
            if arr[i][j] != arr[i][j - 1]:
                arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
                arr_n[j - 1][i], arr_n[j][i] = arr_n[j][i], arr_n[j - 1][i]
                total = max(b(arr[i]), b(arr_n[j-1]), b(arr_n[j]))
                if total == N:
                    return total
                elif max_n < total:
                    max_n = total
                arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
                arr_n[j - 1][i], arr_n[j][i] = arr_n[j][i], arr_n[j - 1][i]
            if arr_n[i][j] != arr_n[i][j - 1]:
                arr_n[i][j - 1], arr_n[i][j] = arr_n[i][j], arr_n[i][j - 1]
                arr[j - 1][i], arr[j][i] = arr[j][i], arr[j - 1][i]
                total = max(b(arr_n[i]), b(arr[j-1]), b(arr[j]))
                if total == N:
                    return total
                elif max_n < total:
                    max_n = total
                arr_n[i][j - 1], arr_n[i][j] = arr_n[i][j], arr_n[i][j - 1]
                arr[j - 1][i], arr[j][i] = arr[j][i], arr[j - 1][i]
    return max_n


def b(arr):
    visited = [1] * N
    for i in range(1, N):
        if arr[i] == arr[i-1]:
            visited[i] = visited[i-1] + 1
    return max(visited)


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
arr_n = list(map(list, zip(*arr)))
print(a())
