# 1748
# 입력: N
# 출력: 1~ N까지의 수를 이어쓴 새로운 수의 자릿수

N = input().strip()
n = len(N)
result = (int(N)-10**(n-1)+1)*n
for i in range(1,n):
    result += 9*i*(10**(i-1))

print(result)