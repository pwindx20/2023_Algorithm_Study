#2548
# 입력: 자연수의 개수 N / N개의 자연수가 빈칸을 사이에 두고 입력
# 출력: 대표 자연수 두개 이상일 경우 그중 제일 작은 것
# 주어진 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의 합을 최소로 하는 자연수
N = int(input())
numbers = sorted(list(map(int,input().split())))
mid = N // 2 if N%2 else (N-1)//2
print(numbers[mid])

# 걍 중앙값인데?