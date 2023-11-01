# 입력: 0~9까지의 숫자 중 일부가 들어있는 정수 배열 numbers
# 출력: 찾을수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
def solution(numbers):
    answer = 45
    for number in numbers:
        answer-=number
    return answer

