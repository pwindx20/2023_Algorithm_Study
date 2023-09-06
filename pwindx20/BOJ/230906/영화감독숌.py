# 1436
# 입력: N
# 출력: N번째 영화의 제목에 들어간 수
# 666이 들어간 숫자 중 N번째 작은 숫자
N = int(input())
cnt = 0
num = 0
while cnt<N:
    num += 1
    if '666' in str(num):
        cnt += 1
print(num)