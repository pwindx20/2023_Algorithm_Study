def solution(babbling):
    
    answer = 0
    
    for elem in babbling:
        if elem  in ['aya', 'ye', 'woo', 'ma']:
            answer += 1
        

    return answer