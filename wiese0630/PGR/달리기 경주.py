players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    for name in callings:
        idx = players.index(name)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return answer


# players[idx], players[idx-1] = players[idx-1], players[idx]
# print(players[idx], players[idx-1])
players[players.index(name)], players[players.index(name)-1] = players[players.index(name)-1], players[players.index(name)]
print(players)
# print(players[players.index(name)], players[players.index(name)-1])
