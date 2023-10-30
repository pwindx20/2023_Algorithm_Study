def solution(X, Y):
    list_x = list(X)
    list_y = list(Y)
    list_ans = []
    for elem in list_x:
        if elem in list_y:
            list_ans.append(elem)
            list_y.remove(elem)
    list_ans.sort(reverse=True)
    answer = '0'
    if list_ans == []:
        answer = '-1'
    elif set(list_ans) == {'0'}:
        answer = '0'
    else:
        answer = ''.join(list_ans)
        
    return answer


# 답은 맞는 것 같은데 시간초과 fail...