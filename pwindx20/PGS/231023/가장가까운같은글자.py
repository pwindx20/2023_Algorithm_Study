# 입력: 문자열 s 
# 출력: 리스트...

def solution(s):
    answer = []
    aph_dic = {}
    for i, a in enumerate(s):
        if a in aph_dic:
            answer.append(i- aph_dic[a])
        else:
            answer.append(-1)
        aph_dic[a] = i 
    return answer

s = 'foobar'
print(solution(s))