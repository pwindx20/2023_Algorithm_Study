# 2587
# 입력: 1~5줄까지 한줄에 하나씩 자연수 100보다 작은 10의 배수
# 출력: 평균/ 중앙값
lst = [int(input()) for _ in range(5)]
print(sum(lst)//5)
print(sorted(lst)[2])