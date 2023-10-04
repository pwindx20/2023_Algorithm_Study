# 1080
# 입력: N, M/ N개의 줄에는 행렬 A가 주어지고 다음 N줄에는 B
# 출력: B로 바꾸는데 필요한 연산 횟수의 최솟값 A를 B로 바꿀 수 없다면 -1
# 3*3 부분 행렬에 있는 모든 원소를 뒤집는다.
def change(r, c):
    for i in range(3):
        for j in range(3):
            A[r+i][c+j]='0' if A[r+i][c+j]=='1' else '1'

def check(x):
    for i in range(x):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False  
    return True


N, M = map(int,input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]
count = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            change(i, j)
            count += 1
    if not check(i):
        count = -1
        break
else:
    if not check(N):
        count = -1

print(count)