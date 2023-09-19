# 14500
# 입력: N, M/ 종이에 쓰여져 있는 수
# 출력: 테트로미노가 놓은 칸에 쓰인 수들의 합의 최댓값

N, M = map(int,input())
base = [list(map(int,input().split())) for _ in range(N)]
