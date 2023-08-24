# 5186
def dectobin(N):
    result = ''
    temp = 0
    i = 0
    while i <=12 and temp <= N:
        if temp ==N:
            return result
        i += 1
        if temp + 2**(-i)<=N:
            temp = temp + 2**(-i)
            result = result + '1'
        else:
            result = result + '0'

    return 'overflow'

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {dectobin(N)}')