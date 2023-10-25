def solution(k, m, score):
    
    score.sort(reverse=True)
    # 사과 가격 내림차순으로 정렬
    
    divided_score = [score[i:i+m] for i in range(0, len(score), m)]
    # m개의 원소를 갖도록 리스트 분할
    
    sum = 0
    for group in divided_score: # 분할한 리스트 중
        if len(group) == m: # 원소 개수가 m개면
            sum += min(group) * m
    
    

    answer =  sum
    return answer