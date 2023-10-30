# 입력: 칼로리가 적은 순서대로 나타내는 정수 배열 food
# 출력: 음식 배치를 나타내는 문자열
# 한 선수는 왼쪽부터 오른쪽 다른 선수는 오른쪽부터 왼쪽
# 중앙에는 물을 배치, 물을 먼저 먹는 선수가 승리
# 두 선수가 먹는 음식의 종류와 양이 같아야하며 음식을 먹는 순서도 같아야함
# 칼로리가 낮은 음식부터 배치
def solution(food):
    ans1 = ''
    ans2 = ''
    for i, num in enumerate(food[1:], start=1):
        ans1 = ans1 + str(i)*(num//2)
        ans2 = str(i)*(num//2) + ans2
    return ans1+'0'+ans2

food = [1, 3, 4, 6]
print(solution(food))