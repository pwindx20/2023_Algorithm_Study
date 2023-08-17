# 2525
# 입력: 현재 시각 A 0~23 B 0~59/ C 0~1000
# 출력: 시 분

A, B = map(int, input().split())
C = int(input())
if B+C>=60:
    newB = (B+C)%60
    newA = (A+(B+C)//60)%24  
else: 
    newB = B+C
    newA = A

print(newA, newB)