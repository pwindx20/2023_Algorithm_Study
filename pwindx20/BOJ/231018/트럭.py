# 13335
# 입력: 다리를 건너는 트럭의 수 n(1~1000), 다리의 길이 w(1~100), 다리의 하중 L(10~1000)/
#       n개의 정수 a1, a2, ...an (i번째 트럭의 무게)
# 출력:  모든 트럭이 다리를 건너는 최단 시간

n, w, L = map(int,input().split())
truck_lst = list(map(int, input().split()))
t = 0
start = 0
index = 0
sumV = 0

while index<n:
    sumV += truck_lst[index]
    if sumV>L:
        t += index-start+w
        start =index
        sumV = truck_lst[start]
    if index-start>w:
        sumV-=truck_lst[start]
        start += 1
    index += 1

if start!= index:
    t += index-start+w
else:
    t += w

print(t)

    