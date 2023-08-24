# 1240
# 입력: t/ 세로크기 N(1~50) 가로크기 M(56~100)/ N*M 배열
# 출력: #tc 암호코드 숫자 합/ 잘못된 암호코드: 0
# 홀수*3 + 짝수

T = int(input())
for tc in range(1,T+1):
    N , M = map(int(input().split()))
    arr = [list(input())]
    for i in range(N):
        if arr[i].count(0)==M:
            continue
        else:
            code = arr[i]