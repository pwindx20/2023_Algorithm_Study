# 입력: 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열 배열 keymap
#       입력하려는 문자열들이 담긴 문자열 배열 targets
# 출력: 문자열 작성을 위해 키를 최소 몇번 눌러야하는지 순서대로 배열에 담아 return/ 작성할 수 없다면 -1
# 
def solution(keymap, targets):
    keydict = {}
    for key in keymap:
        for i, k in enumerate(key, start=1):
            if k not in keydict:
                keydict[k] = i
            else:
                if keydict[k] > i:
                    keydict[k] = i
    
    answer = []
    
    for target in targets:
        temp = 0
        for t in target:
            if t in keydict:
                temp += keydict[t]
            else:
                temp = -1
                break
        answer.append(temp)
    
    return answer

km = ["AA"]
targets = 	["B"]
print(solution(km, targets))