# 입력: name- 이름 yearning - 그리움 점수 photo- 이름을 담은 2차원 문자열 배열
# 출력: 점수를 순서대로 출력

def solution(name, yearning, photo):
    answer = []
    yearning_dict = {}
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
        
    for people in photo:
        temp = 0
        for person in people:
            if person in name:
                temp += yearning_dict[person]
        answer.append(temp)
    return answer