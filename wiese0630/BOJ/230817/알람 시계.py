H, M = map(int, input().split())

if M >= 45:
    M = M-45
else:
    M = M+15
    H = H-1
if H < 0:
    H = H+24
print(H, M)