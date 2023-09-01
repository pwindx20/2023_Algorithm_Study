# 2720
# 입력: T/ 거스름돈 C(1~500) 센트
# 출력: 동전 개수
# 쿼터: 0.25, 다임:0.1, 니켈:0.05, 페니:0.01
T = int(input())
for _ in range(T):
    C = int(input())
    print(C//25, end=' ')
    C = C % (25)
    print(C//10, end=' ')
    C = C % (10)
    print(C//5, end=' ')
    C = C % (5)
    print(C)
    