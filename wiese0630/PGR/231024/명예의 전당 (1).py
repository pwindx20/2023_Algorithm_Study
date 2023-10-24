def solution(k, score):
    answer = []
    if k > len(score) :
        k = len(score)
        
    for idx in range(1,k+1):
        answer.append(min(score[:idx]))
    
    
    for idx in range(k+1, len(score)+1):
        new_score = score[:idx]
        new_score.sort(reverse=True)        
        answer.append(new_score[k-1])
    return answer

