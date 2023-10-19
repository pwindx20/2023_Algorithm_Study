# 입력: 문자열로 이루어진 배열 card1, card2, 원하는 단어 배열 goal
# 출력: card1과 card2에 적힌 단어들로 goal을 만들수 있으면 "Yes", 아니면 'No' return
# 원하는 카드 뭉치에서 순서대로 한장씩 사용
# 한번 사용한 카드는 다시 사용 X
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다
# 기존에 주어진 카드 뭉치의 단어순서는 바꿀 수 없다
def solution(cards1, cards2, goal):
    answer = ''
    w1, w2 = cards1.pop(0), cards2.pop(0)
    for word in goal:
        if word == w1:
            w1 = cards1.pop(0) if cards1 else ''
        elif word == w2:
            w2 = cards2.pop(0) if cards2 else ''
        else:
            answer = 'No'
            break
    else:
        answer = 'Yes'
    return answer

card1 = ["i", "water", "drink"]
card2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(card1, card2, goal))