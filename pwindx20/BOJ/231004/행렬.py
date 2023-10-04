# 1080
# 입력: N, M/ N개의 줄에는 행렬 A가 주어지고 다음 N줄에는 B
# 출력: B로 바꾸는데 필요한 연산 횟수의 최솟값 A를 B로 바꿀 수 없다면 -1
# 3*3 부분 행렬에 있는 모든 원소를 뒤집는다.

N, M = map(int,input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

