# 2485
# 입력: 이미 심어진 가로수의 수 N/ N개 줄에는 각줄마다 심어진 가로수 위치
#       가로수의 위치를 나타내는 정수는 모두 다르고, N개의 가로수는 기준점으로부터 떨어진 거리가 가까운 순서대로 주어진다.
# 출력: 같은간격이 되도록 새로 심어야하는 가로수의 최소 수
import sys
N = int(sys.stdin.readline())
trees = [int(sys.stdin.readline()) for _ in range(N)]
min_distance = 10000000000000000000000000000

for i in range(1, N):
    distance = trees[i]-trees[i-1]
    print(distance, end=' ')
    
    if min_distance>distance:
        if min_distance%distance ==0:
            min_distance = distance
        else:
            a, b = min_distance, distance
            while b>0:
                a, b = b, a%b
            min_distance = a
    else:
        if distance%min_distance:
            if min_distance%distance ==0:
                min_distance = distance
        else:
            a, b = min_distance, distance
            while b>0:
                a, b = b, a%b
            min_distance = a

print(min_distance)
print((trees[-1]-trees[0])//min_distance-N+1)