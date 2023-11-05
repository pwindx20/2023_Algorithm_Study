def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        n = int(i ** 0.5)
        if n == i / n:
            answer -= i
        else:
            answer += i
    return answer