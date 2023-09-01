# 2444
N = int(input())
for i in range(N):
    print(' '*(N-1-i),end='')
    print('*'*(i*2+1))
for j in range(1, N):
    print(' '*j, end='')
    print('*'*(2*(N-1-j)+1))