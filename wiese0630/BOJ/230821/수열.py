N = int(input())
lst = list(map(int, input().split()))
cnt = 1
anslist = []
for i in range(N - 1):
    while lst[i] < lst[i + 1]:
        cnt += 1
        if lst[i] == lst[i + 1]:
            cnt += 1
        else:
            anslist.append(cnt)
            cnt = 1
            break

    while lst[i] > lst[i + 1]:
        cnt += 1
        if lst[i] == lst[i + 1]:
            cnt += 1
        else:
            anslist.append(cnt)
            cnt = 1
            break

    if lst[i+1] == N:
        anslist.append(cnt)
    #수열이 계속 증가하거나 감소하는 경우 cnt값을 어떻게 처리해야할 지 모르겠음....
print(max(anslist))



