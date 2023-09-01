# 2675
# 입력: T/ 반복횟수 R(1~8), 문자열 S(1~20글자)
# 출력: R번 반복해 새문자열 P를 만든 후 출력

T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    answer = ''
    for s in S:
        answer = answer + s*int(R)
    print(answer)