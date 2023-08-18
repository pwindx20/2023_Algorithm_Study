# 12712
# 입력: T/ 배열 N(5~15), 스프레이 세기 M (2~N)/ 파리마리수
# 출력: #t 최대 합

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    