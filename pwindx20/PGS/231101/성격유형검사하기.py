# 입력: 질문마다 판단하는 지표를 담은 1차원 배열 survey 
# 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices
# 출력: 유형검사결과를 지표 번호 순서대로
# 매우동의/매우비동의 3점 동의/비동의 2점 약곤동의/약간비동의 1점 모르겠음 0점
# 더 높은 점수를 받은 성격유형
# 1, 2, 3, 4, 5, 6, 7,=> 매우비동의 비동의 약간비동의 모르겠음 약간동의 동의 매우동의
def solution(survey, choices):
    answer = ''
    N = len(survey)
    ctg = {'A':0, 'N':0, 'C':0, 'F':0, 'J':0, 'M':0, 'R':0, 'T':0}
    score = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    for i in range(N):
        if choices[i] >4:
            ctg[survey[i][1]] += score[choices[i]]    
        elif choices[i] <4:
            ctg[survey[i][0]] += score[choices[i]]

    answer = answer + 'R' if ctg['R']>=ctg['T'] else answer + 'T'
    answer = answer + 'C' if ctg['C']>=ctg['F'] else answer + 'F'
    answer = answer + 'J' if ctg['J']>=ctg['M'] else answer + 'M'
    answer = answer + 'A' if ctg['A']>=ctg['N'] else answer + 'N'
    return answer


'''
    ctg = {'AN':0, 'CF':0, 'JM':0, 'RT':0}
    for  i in range(N):
        if survey[i] in 'ANA':
            if survey[i][0] == 'A':
                if choices[i] == 7:
                   ctg['AN'] -= 3 
                elif choices[i] == 6:
                   ctg['AN'] -= 2 
                elif choices[i] == 5:
                   ctg['AN'] -= 1 
                elif choices[i] == 3:
                   ctg['AN'] += 1 
                elif choices[i] == 2:
                   ctg['AN'] += 2 
                elif choices[i] == 1:
                   ctg['AN'] += 3 
        elif survey[i] in 'CFC':
            if survey[i][0] == 'C':
                if choices[i] == 7:
                   ctg['AN'] -= 3 
                elif choices[i] == 6:
                   ctg['AN'] -= 2 
                elif choices[i] == 5:
                   ctg['AN'] -= 1 
                elif choices[i] == 3:
                   ctg['AN'] += 1 
                elif choices[i] == 2:
                   ctg['AN'] += 2 
                elif choices[i] == 1:
                   ctg['AN'] += 3
'''

# 다른 사람 풀이 
'''
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

'''