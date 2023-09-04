import sys
sys.stdin = open('input2477.txt', 'r')

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
print(arr)

listw = []
listl = []

for i in range(6):
    if arr[i][0] in [1, 2]: #방향을 나타내는 수가 1, 2이면
        listl.append(arr[i][1])
    else: #방향을 나타내는 수가 2, 3이면
        listw.append(arr[i][1])

# print(listw)
# print(listl)

# listw.remove(0)
#
#
#
# listl.append(arr[3][0])
# listl.append(arr[3][1])
# listl.append(arr[4][0])
# listl.append(arr[4][1])
# listl.remove(0)
#
#
# big_square = max(listw) * max(listl)
# print(big_square)
# small_square = min(listw) * min(listl)
# print(small_square)
# real_square = big_square - small_square
#
# ans = real_square * K
#
# print(ans)