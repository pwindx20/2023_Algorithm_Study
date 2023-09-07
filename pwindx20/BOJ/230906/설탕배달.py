# 2839
# 입력: N
# 출력: 최대한 적은 봉지 , 정확히 N킬로그램을 만들 수 없다면 -1을 출력한다.

N = int(input())
num1 = N//5
num2 = N//3
cnt = 100000
for i in range(num1+1):
    for j in range(num2+1):
        if 5*i + 3*j == N:
            if cnt > i+j:
                cnt = i+j
print(cnt) if cnt !=100000 else print(-1) 