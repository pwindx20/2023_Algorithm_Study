lst = list(map(int, input().split()))

if max(lst) < sum(lst) - max(lst):
    print(sum(lst))
else:
    print(2*sum(lst) - 2*max(lst) - 1)

