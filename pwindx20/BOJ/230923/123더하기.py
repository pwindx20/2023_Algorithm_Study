# 9095
# 입력: T/ n(<11)
# 출력: n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
def solve(sumv):
    global cnt
    if sumv >n:
        return
    
    if sumv == n:
        cnt+=1
        return
    
    for i in [1, 2, 3]:
        solve(sumv+i)

T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    solve(0)
    print(cnt)