# 5203
# 입력: T(1~50)/ 0~9 사이인 12개의 숫자
# 출력: #t 승리: 1, 2 무승부: 0
# 연속인 숫자가 3개 이상 run 같은 숫자가 3개이상 triplet
# 플레이어 1과 2가 번갈아가며 카드를 가져감
def game(lst):
    player1=[0]*10
    player2=[0]*10
    for i in range(6):
        player1[lst[2*i]] += 1
        
        if player1.count(3):
            return 1
        for j in range(8): # range 잘못써서 한번 틀림
            if player1[j] and player1[j+1] and player1[j+2]:
                return 1
        
        player2[lst[2*i+1]] +=1

        if player2.count(3):
            return 2
        for j in range(8):
            if player2[j] and player2[j+1] and player2[j+2]:
                return 2
    else:
        return 0       

        
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int,input().split()))
    print(f'#{tc} {game(cards)}')