E, S, M = map(int, input().split())

#이해를 못하겠움
newE = 0
newS = 0
newM = 0
for e in range(1000):
    for s in range(1000):
        for m in range(1000):
            newE = E + 15*e
            newM = M + 19*m
            newS = S + 28*s
            if newE == newM and newM and newS:
                print(newE)
            break
        break
    break

