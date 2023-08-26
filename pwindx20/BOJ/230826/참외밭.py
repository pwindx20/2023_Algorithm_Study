# 2477
# 입력: 참외의 개수 K(1~20)/ 반시계방향 둘레를 돌면서 지나는 변의길이와 방향의 길이 
#       1: 동쪽 2: 서쪽 3: 남쪽 4: 북쪽
# 출력: 밭에 자라는 참외의 수

K = int(input())
direction = ''
lines = []

for i in range(6):
    d, line = input().split()
    direction = direction + d
    lines.append(int(line))

direction = 2*direction
lines = 2*lines
answer = 0

if '3131' in direction:
    answer = lines[direction.index('2')] * lines[direction.index('4')]-lines[direction.index('3131')+1]*lines[direction.index('3131')+2]
elif '4242' in direction:
    answer = lines[direction.index('3')] * lines[direction.index('1')]-lines[direction.index('4242')+1]*lines[direction.index('4242')+2]
elif '2323' in direction:
    answer = lines[direction.index('1')] * lines[direction.index('4')]-lines[direction.index('2323')+1]*lines[direction.index('2323')+2]
elif '1414' in direction:
    answer = lines[direction.index('2')] * lines[direction.index('3')]-lines[direction.index('1414')+1]*lines[direction.index('1414')+2]

print(answer*K)