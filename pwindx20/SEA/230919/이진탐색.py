# 5207
# 입력: T/ N, M/ N, M개의 정수
# 출력: #T 양쪽을 번갈아가며 탐색하는 수
def solve(s, e, target, rl):
    global cnt
    m = (s+e)//2
        
    if s>e:
        return

    if arr[m] == target:
        # print(target)
        cnt += 1
    elif arr[m] < target and rl<=0:
        solve(m+1, e, target, 1)
    elif arr[m] > target and rl>=0:
        solve(s, m-1, target, -1)
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    nums = list(map(int,input().split()))
    cnt = 0
    for num in nums:
        # print(num)
        solve(0, N-1, num, 0)
    print(f'#{tc} {cnt}')