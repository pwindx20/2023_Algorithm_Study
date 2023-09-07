# 25305
# 입력: N, 상을 받는 사람 수 k/ 각 학생의 점수 x
# 출력: 상을 받는 사람 중 가장 낮은 점수

N, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)
print(score[k-1])