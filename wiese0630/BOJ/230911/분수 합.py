import sys

N1, M1 = map(int, sys.stdin.readline().split())
N2, M2 = map(int, sys.stdin.readline().split())

N3, M3 = N1*M2, M1*M2
N4, M4 = N2*M1, M2*M1

ans1 = N3+N4
ans2 = M3


while ans1 > 0:
    t = ans2 % ans1
    ans2 = ans1
    ans1 = t
    

gcd = ans2

print(N3+N4//gcd, M3//gcd)


