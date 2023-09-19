N = int(input())
lst = list(map(int, input().split()))
ST = []
start = 1
for i in range(N):
    if start != lst[i]:
        ST.append(lst[i])
    else:
        start += 1
    while ST:
        if ST[-1] == start:
            ST.pop()
            start += 1
        else:
            break
if not ST:
    print('Nice')
else:
    print('Sad')

# 대기열을 다 채우고 시작하는게 아님@