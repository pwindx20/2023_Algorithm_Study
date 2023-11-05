def solution(left, right):
    answer = 0
    for divid in range(left, right+1):
        yaksoo = 0
        for divis in range(1, divid+1):
            if divid % divis == 0:
                yaksoo += 1
        if yaksoo % 2 == 0:
            answer += divid
        else:
            answer -= divid

    return answer