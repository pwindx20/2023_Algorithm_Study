def solution(absolutes, signs):
    sum = 0
    
    for idx in range(len(absolutes)):
        if signs[idx] is True:
            sum += absolutes[idx] 
        else:
            sum -= absolutes[idx]
    return sum