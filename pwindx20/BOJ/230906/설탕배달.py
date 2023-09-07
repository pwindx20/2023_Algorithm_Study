# 2839
# 입력: N
# 출력: 최대한 적은 봉지 , 정확히 N킬로그램을 만들 수 없다면 -1을 출력한다.

N = int(input())
answer =0
answer += N//5
etc = N%5
if etc%3 !=0:
    print(-1)
else: print(answer+etc//3)