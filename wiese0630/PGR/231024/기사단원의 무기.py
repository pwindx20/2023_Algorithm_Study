number = 10
limit = 3
power = 2

import math 

def solution(number, limit, power):
    numbers = [0] * (number+1)
    for num1 in range(1, number+1):
        for num2 in range(1, int(math.sqrt(num1))+1):
            if num1 % num2 == 0:
                numbers[num1] += 1
         
    print(numbers)
    for idx in range(number):
        if numbers[idx] > limit:
            numbers[idx] = power

    answer = sum(numbers)
    return answer

print(solution(number, limit, power))