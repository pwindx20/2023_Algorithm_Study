# 6064
# 입력: T/ M, N, x, y (M:N 은 카잉 달력의 마지막 해)
# 출력: <x,y>가 k번째 해 (만약 x:y에 의해 표현되는 해가 없다면 -1 출력)
def solve():
    for i in range(N):
        if (i*M+x)%N==y%N:
            return i*M+x
    return -1
    
T = int(input())
for tc in range(1, T+1):
    M, N, x, y = map(int,input().split())
    if M>N:
        M, N, x, y = N, M, y, x
    print(solve())