def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i ** 0.5 == j and j != 1:
                cnt += 1
            elif not i % j:
                cnt += 2
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer


print(solution(10, 3, 2))