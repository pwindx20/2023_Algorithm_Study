# 2529
# 입력: 부등호 개수/ 부등호(띄어쓰기 유)
# 출력: 최대, 최소 값
# 선택된 숫자는 모두 달라야한다.
def solve(k):
    global maxv, minv, result1, result2
    if k>=2:
        if lst[k-2]=='>' and result[k-2]<result[k-1]:
            return
        if lst[k-2]=='<' and result[k-2]>result[k-1]:
            return
    
    if k==N+1:
        ans = ''.join(map(str, result))
        if int(ans)>maxv:
            maxv = int(ans)
            result1=ans
        if int(ans)<minv:
            minv = int(ans)
            result2=ans
        return

    for i in range(10):
        if not used[i]:
            used[i] = True
            result.append(i)
            solve(k+1)
            result.pop()
            used[i] = False

N = int(input())
lst = input().split()
used = [False]*10
result = []
minv = 9999999999
maxv = 0
result1 = ''
result2 = ''
solve(0)
print(result1)
print(result2)