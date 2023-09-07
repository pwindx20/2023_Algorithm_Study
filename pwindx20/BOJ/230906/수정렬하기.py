# 2750
# 입력: N/ N개의 줄에 수
# 출력: 오름차순으로 정렬한 결과를 한줄에 하나씩
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
for i in range(N):
    print(lst[i])
    