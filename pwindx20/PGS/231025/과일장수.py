# 입력: 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score
# 출력: 과일 장수가 얻을 수 있는 최대 이익
# 한 상자에 사과를 m개씩 포장, 상자에 담긴 사과 중 가장 낮은 점수 p*m
# 남는 사과는 버림...
def solution(k, m, score):
    answer = 0
    N = len(score)
    score.sort()
    if N%m:
        n = N%m
        score = score[n:]

    for i in range(0, N//m*m, m):
        answer += score[i]*m
    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))