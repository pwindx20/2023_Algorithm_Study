# 10773
# 입력: K/ k줄에 정수 1개씩/ 정수가 '0'일 경우 가장 최근에 쓴 수를 지우고 아닐 경우 해당 수를 쓴다
# 출력: 최종적으로 적어 낸 수의 합
import sys
K = int(sys.stdin.readline())
ST = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        ST.pop()
    else:
        ST.append(num)
print(sum(ST))
