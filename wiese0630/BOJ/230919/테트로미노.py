#상하좌우
move = [(0,1), (0, -1), (1, 0), (-1, 0)]

# input
N, M = map(int, input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최대값 초기화
maxValue = 0


#이 이후로 이해를 포기함...
#일단 테트로미노의 모양이 델타로 이동해서 만들 수 있다는 건 알겠움 SWEA에 비슷한 문제 있음