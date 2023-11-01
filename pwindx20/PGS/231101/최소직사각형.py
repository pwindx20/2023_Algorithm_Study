# 입력: 모든 명함의 가로길이와 세로길이를 나타내는 2차원 배열 sizes
# 출력: 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기

def solution(sizes):
    maxW, maxH = 0, 0
    for size in sizes:
        w, h = max(size), min(size)
        if maxW < w:
            maxW = w
        if maxH < h:
            maxH = h
    answer = maxW*maxH
    return answer

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

print(solution(sizes))