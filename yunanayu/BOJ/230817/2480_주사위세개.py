A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A == B or B == C:
    print(1000 + 100 *B)
elif C == A:
    print(1000 + 100 * A)
else:
    print(max(A,B,C)*100)