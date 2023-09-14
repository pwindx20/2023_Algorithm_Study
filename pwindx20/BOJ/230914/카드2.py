# 2164
# 입력: N
# 출력: 첫째 줄에 남게 되는 카드의 번호 출력
from collections import deque

N = int(input())
cards = deque(range(1, N+1))
cnt = 1
while cards:
    v = cards.popleft()
    if cnt%2==0:
        cards.append(v)
    cnt+=1
print(v)


########## 7일때 2가 나와야함#################
# N = int(input())
# i = 0
# while N>=(1<<i):
#     i+=1
# print(1<<(i-1))


###다른 사람 풀이 -- 굳이 2로 나눌필요 없이 그냥 두번 쓰면 되는거였구나...
# from collections import deque
# N = int(input())
# myQueue = deque()

# for i in range(1, N+1):
#     myQueue.append(i)

# while len(myQueue) > 1:
#     myQueue.popleft()
#     myQueue.append(myQueue.popleft())

# print(myQueue[0])