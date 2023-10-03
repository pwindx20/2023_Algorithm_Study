def sol(N):
    result = ''
    num = 0
    for i in range(len(N)):
        num += int(N[i])
    for n in N:
        result += n
    if '0' not in N:
        return -1
    elif num%3 != 0:
        return -1
    else:
        return int(result)




N = list(input())
N.sort()
N.reverse()

print(sol(N))