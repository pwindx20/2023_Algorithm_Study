# 15038. 4881 배열 최소 합
# 입력: T 1~50/ N 3~10/ 10보다 작은 자연수 N개 N줄
# 출력: #t 합이 최소가 되는 숫자... 같은 세로, 가로에선 고를 수 없다

# 와.... 순열 아예 기억이 안나는데?


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False]*N
    ST = []
    result = 
    