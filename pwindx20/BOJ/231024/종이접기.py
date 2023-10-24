# 1802
# 입력: T/ 1: OUT 0: IN 띄어쓰기 X 문자열의 길이 3000보다 작다 항상 2^N-1
# 출력: T개의 줄에 동호의 방법대로 다시 접을 수 있으면 YES 없으면 NO
# 반시계방향, 시계방향으로 접는 2가지 방법
def solution(s, e):
    global ans
    if ans == 'NO':
        return
    
    if s==e:
        return
    
    m = (s+e)//2
    
    for i in range(m-s):
        if paper[i] == paper[e-i]:
            ans = 'NO'
    
    solution(s, m-1)
    solution(m+1, e)
    
T = int(input())
for _ in range(T):
    paper = input()
    # 가운데를 기준으로 좌우 반전
    ans = 'YES'
    solution(0, len(paper)-1)
    print(ans)