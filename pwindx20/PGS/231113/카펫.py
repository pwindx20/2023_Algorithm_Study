def solution(brown, yellow):
    total = brown+yellow
    isF = False
    for i in range(3, brown//2):
        for j in range(brown//2-1, 2, -1):
            if i*j == total and (i-2)*(j-2)==yellow:
                isF = True
                break
        if isF:
            break
    answer = [max(i, j), min(i, j)]
    return answer

b = 4004
y = 999999
print(solution(b, y))