A, B = map(int, input().split())
N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())
print(pos)


# 경비원
'''
시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
반시계방향
dr = [1, 0, 1, 0]
dc = [0, -1, 0, 1]
'''


A, B = map(int, input().split())    # 블록 크기 가로x세로
N = int(input())    #   상점의 개수
pos = [list(map(int, input().split())) for _ in range(N)]   # 상점 N개의 위치
X, Y = map(int, input().split())        # 동근이의 위치
# print(pos)