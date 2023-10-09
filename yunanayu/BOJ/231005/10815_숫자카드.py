
def search(num):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] > num:
            end = middle -1
        elif lst[middle] < num:
            start = middle + 1
        else:
            return 1
    return 0


N = int(input())
lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
lst.sort()
for m in M_lst:
    print(search(m), end=' ')



# for m in M_lst:
#     if m in lst:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
    # print(lst)
# print(M_lst)