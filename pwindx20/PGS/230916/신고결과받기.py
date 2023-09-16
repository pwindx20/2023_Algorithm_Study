# 입력: 이용자의  id가 담긴 문자열배열 id_list, 각 이용자가 신고한 이용자의 id정보가 담긴 문자열 배열 report, 정지기준이 되는 신고 횟수 k
# 출력: 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

def solution(id_list, report, k):
    
    # 이용자의 아이디가 담긴 딕셔너리
    user_dict = dict()
    mail = dict()
    for i in id_list:
        user_dict[i] = set() 
        mail[i] = 0

    # 신고당한 id: set(신고한 이용자의 id)
    for ids in report:
        id1, id2 = ids.split()
        user_dict[id2].add(id1)
    
    for user in id_list:
        if len(user_dict[user])>=k:
            for j in user_dict[user]:
                mail[j] += 1
    
    return list(mail.values())