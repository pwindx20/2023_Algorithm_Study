def solution(ingredient):
    answer = 0
    slot = []
    for elem in ingredient:
        slot.append(elem)
        if slot[-4:] == [1, 2, 3, 1]:
            answer += 1
            slot.pop()
            slot.pop()
            slot.pop()
            slot.pop()
    
    return answer