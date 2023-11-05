def solution(numbers):
    answer = 0
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in sample:
        if number not in numbers:
            answer += number
    return answer