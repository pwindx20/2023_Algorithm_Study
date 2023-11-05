def solution(sizes):
    answer = 0
    list_min = []
    list_max = []
    for size in sizes:
        list_min.append(min(size))
        list_max.append(max(size))
    answer = max(list_max) *  max(list_min)
    return answer