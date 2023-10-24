# 입력: 명예의 전당 목록의 점수 개수 k, 1일부터 마지막날까지 출연한 가수들의 점수 score
# 출력: 매일 발표된 명예의 전당의 최하위 점수
def solution(k, score):
    answer = []
    ranking = []
    minS = -1
    for s in score:
        if len(ranking)>= k:
            if s>minS:
                ranking.append(s)
                ranking.sort()
                ranking.pop(0)
        else:
            ranking.append(s)
            ranking.sort()
        minS = ranking[0]
        answer.append(minS)
        print(ranking)
    return answer

k = 2
score =[10, 0, 0, 0, 0, 0, 0]
print(solution(k, score))



########## 다른 사람 풀이
### 굳이 범위를 안나누고 그냥... 넣고 제일 작은걸 빼버림... 이건 데이터 범위가 생각보다 작아서 ㄱㅊ을듯
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer