def solution(s):
    l = len(s)
    answer = [-1] * l
    d = {}
    for i in range(l):
        d.setdefault(s[i], -1)
        if d[s[i]] == -1:
            d[s[i]] = i
        else:
            answer[i] = i - d[s[i]]
            d[s[i]] = i
    return answer