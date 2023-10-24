# 입력: 왼쪽에서 오른쪽으로 읽어나가면서 x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다.
# 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
# s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복
# 두 횟수가 다른 상태에서 더이상 읽을 글자가 없다면 종료
# 출력: 분해한 문자열의 개수

def solution(s):
    answer = 0
    xcount = 0
    ncount = 0
    for a in s:
        if xcount==ncount:
            x = a
            answer += 1
            xcount += 1
        else:
            if x==a:
                xcount += 1
            else:
                ncount += 1
        
    return answer

s = 'abracadabra'
print(solution(s))