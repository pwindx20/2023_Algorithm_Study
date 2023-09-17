#15033. 4880 토너먼트 카드게임
# 입력: T (1~50)/ N(4~100)/ N명의 카드 1: 가위 2: 바위 3: 보
# 출력: #t 1등의 번호
def win(a, b):
    if cards[a] == cards[b]:
        return a
    elif cards[a] < cards[b]:
        if cards[a] == 1 and cards[b] == 3:
            return a
        else:
            return b
    else:
        if cards[a] == 3 and cards[b] == 1:
            return b
        else:
            return a
        
def game(s, e):
    if e-s <=1:
        return win(s, e)
    else:
        return win(game(s, (s+e)//2), game((s+e)//2+1,e))
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    print(f'#{tc} {game(1, N)}')