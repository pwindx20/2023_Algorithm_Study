# 1157
# 입력: 알파벳 대소문자
# 출력: 가장 많이 사용된 알파벳을 대문자로 출력, 여러개일시 ? 출력
S = list(input().upper())
N = dict()
for s in set(S):
    cnt = S.count(s)
    if cnt in N:
        print('?') # 반례 Cbtt 해결방안 고민중! 
        break
    else:
        N[cnt]=s
else:
    print(N[max(N.keys())])