# 입력: 두 정수 X, Y
# 출력: X, Y의 짝꿍 존재하지 않으면 -1
# 두 정수의 임의의 자리에서 공통으로 나타나는 정수 k(0~9)들을 이용하여 만들 수 있는 가장 큰 정수=두 수의 짝꿍
# X, Y 자릿수가 무지 김
def solution(X, Y):
    answer = ''
    numX = {'9':0, '8':0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0':0}
    numY = {'9':0, '8':0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0':0}
    
    for x in X:
            numX[x] += 1

    for y in Y:
            numY[y] += 1
            
    for x in numX.keys():
        # print(x)
        if x in numY:
            answer = answer + x * min(numX[x], numY[x])
    if answer == '':
        answer = '-1'
    if answer.count('0') == len(answer):
        answer = '0'
    return answer 


X = '100'
Y = '2345'
print(solution(X, Y))
'''
def solution(X, Y):
    answer = ''
    numbers = []
    cnt = 0
    for y in Y:
        if y in X:
            X.replace(y,'',1)
            numbers.append(y)
            cnt += 1
    if cnt:
        if numbers.count('0')==cnt:
            answer = '0'
        else:
            answer = answer.join(sorted(numbers, reverse=True))
    else:
        answer = '-1'
    return answer
'''

# 다른 사람 풀이
'''
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
        '''
# 오.... 안터지네