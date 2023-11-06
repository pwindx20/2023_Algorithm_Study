def solution(lottos, win_nums):
    num_w = 0
    num_joker = 0
    best = 0
    worst = 0
    for lotto in lottos:
        if lotto in win_nums:
            num_w += 1
        elif lotto == 0:
            num_joker += 1
    if num_w == 6:
        worst = 1
        best = 1
    elif num_w == 5:
        worst = 2
        best = worst - num_joker
    elif num_w == 4:
        worst = 3
        best = worst - num_joker
    elif num_w == 3:
        worst= 4
        best = worst - num_joker
    elif num_w == 2:
        worst = 5
        best = worst - num_joker
    else:
        worst = 6
        best = worst - num_joker
        if best == 0:
            best = 1
    answer = [best, worst]
    return answer