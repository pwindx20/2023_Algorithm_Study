# 입력: 기사단원의 수 number, 이웃나라의 협약으로 정해진 공격력의 제한수치 limit, 제한수치를 초과한 기사가 사용할 무기의 공격력 power
# 출력: 철의 무게
# 약수의 개수에 해당하는 공격력을 가진 무기 구매 공격력의 제한수치를 정하고 제한수치보다 큰 공격력을 가진 무기를 구매시 협약기관에서 정한 무기 구매
# 1공격력당 1kg 철
def solution(number, limit, power):
    answer = 0
    arr = [0]*(number+1)
    for i in range(1, number+1):
        j = 1
        while i*j<=number:
            arr[i*j] += 1
            # print(i, j, arr)
            j += 1
    for idx, num in enumerate(arr):
        if num>limit:
            arr[idx] = power
    answer = sum(arr)
    # print(arr)
    return answer

number = 10
limit = 2
power = 1
print(solution(number, limit, power))


##### 다른 사람 풀이

def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])