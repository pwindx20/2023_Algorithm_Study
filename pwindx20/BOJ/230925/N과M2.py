# 15650
# 입력: N, M
# 출력: 중복없이 M개를 고른 수열, 오름차순
def solve(n, r, ans):
    if n==len(nums):
        if len(ans)==r:
            print(*ans)
        return
    ans.append(nums[n])
    solve(n+1, r, ans)
    ans.pop()
    solve(n+1, r, ans)
    
N, M = map(int,input().split())
nums = list(range(1, N+1))
solve(0, M, [])

# 조합 어렵네 .... 