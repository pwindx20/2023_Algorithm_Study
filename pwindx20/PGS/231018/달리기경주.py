# 입력: 현재 등수 players, 해설진이 부른 이름을 담은 문자열 배열 callings
# 출력: 1등부터 순서대로 배열을 return
# def solution(players, callings):
#     for call in callings:
#         i = players.index(call)
#         players[i], players[i-1] = players[i-1], players[i]
#     return players

def solution(players, callings):
    players_rank = {}
    rank_players = {}
    N = len(players)
    for i in range(N):
        players_rank[players[i]] = i
        rank_players[i] = players[i]
    for call in callings:
        temp = players_rank[call]
        rank_players[temp], rank_players[temp-1] = rank_players[temp-1], rank_players[temp]
        players_rank[call], players_rank[rank_players[temp]] = players_rank[rank_players[temp]], players_rank[call]
    answer = []
    for indx in range(N):
        answer.append(rank_players[indx])
    return answer


pl = ["mumu", "soe", "poe", "kai", "mine"]
c = ["kai", "kai", "mine", "mine"]
print(solution(pl, c))



#### 다른 사람 풀이 #####
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players