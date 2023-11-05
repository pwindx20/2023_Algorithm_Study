def solution(n):
    if n % 2:
        return 2
    else:
        for i in range(3, n, 2):
            if n % i == 1:
                return i