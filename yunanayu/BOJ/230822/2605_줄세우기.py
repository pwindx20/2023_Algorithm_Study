N = int(input())
lst = list(map(int, input().split()))
# print(lst)
new_list = []
for i in range(N):
    new_list.insert(lst[i], i+1)
print(*new_list[::-1])

