# 2292
# 입력: N (1~1,000,000,000)
# 출력: 최소 개수의 방을 지나서 갈때 몇개의 방을 지나는지 출력
N = int(input())
i = 0
while True:
    if N<=3*i*(i+1)+1:
        print(i+1)
        break
    i+=1