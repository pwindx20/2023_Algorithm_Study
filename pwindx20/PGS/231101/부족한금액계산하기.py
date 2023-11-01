# 입력: 놀이기구의 이용료 price(1~2500) 가지고 있던 금액 money(1~1,000,000,000) 
# 놀이기구 이용횟수 count(1~2500)
# 출력: 얼마가 모자라는지 return 부족하지 않으면 0
# count번째 이용시 원래 이용료의 N배
def solution(price, money, count):
    answer = price*sum(range(count+1))-money
    return answer if answer<0 else 0