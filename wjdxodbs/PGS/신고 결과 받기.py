def solution(id_list, report, k):
    new_report = set(report)
    answer = [0] * len(id_list)
    d = {x: 0 for x in id_list}
    for i in new_report:
        a, b = i.split()
        d[b] += 1
        
    for i in new_report:
        a, b = i.split()
        if d[b] >= k:
            answer[id_list.index(a)]+=1
    return answer