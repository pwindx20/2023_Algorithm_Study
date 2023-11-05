def solution(price, money, count):
    answer = -1
    total_price = price * (1+count)*count/2
    answer = total_price - money
    if answer < 0:
        answer = 0

    return answer