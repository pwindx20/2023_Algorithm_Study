# 5622
S = input()
answer = 0
for s in S:
    if s in 'PQRSTUVWXYZ':
        if s in 'PQRS':
            answer += 8
        elif s in 'TUV':
            answer += 9
        else:
            answer += 10
    else:
        answer += (ord(s)-56)//3
print(answer)