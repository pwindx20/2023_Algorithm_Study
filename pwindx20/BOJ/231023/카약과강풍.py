# 2891
# 입력: 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R/ 
#       카약이 손상된 팀의 번호 (중복 X) / 카약을 하나 더 가져온 팀의 번호 (중복 X)
# 출력: 출발할 수 없는 팀의 최솟값

N, S, R = map(int, input().split())
arr = [1]*(N+1) # 카약의 개수

for i in input().split():
    arr[int(i)] -= 1
for j in input().split():
    arr[int(j)] += 1

# print(arr)

for ix, v in enumerate(arr[1:], start=1):
    if not v:
        if ix != 1 and arr[ix-1] >1:
            arr[ix] += 1
            arr[ix-1] -= 1
        elif ix != N and arr[ix+1]>1:
            arr[ix] += 1
            arr[ix+1] -= 1

# print(arr)
print(arr[1:].count(0))