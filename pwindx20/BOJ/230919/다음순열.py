# 10972
# 입력: N/ 순열
# 출력: 다음 순열...
def per(k, target):
    if k==N+1:
        print(result)
        return
    for i in range(1,N+1):
        if not used[i]:
            result[k] = i
            used[i] = True
            per(k+1, target)
            used[i] = False

N = int(input())
arr = list(map(int,input().split()))
result = [-1]*(N+1)
used = [False]*(N+1)
per(1, arr)