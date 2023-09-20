# 부등호 문자의 개수 k 입력
k = int(input())

# 부등호 문자열 입력
inequalities = input().split()

# 0부터 9까지의 숫자 리스트
numbers = list(range(10))

# 사용된 숫자를 저장할 배열
used = [False] * 10

# 최댓값을 구하는 함수
def find_max(inequalities, numbers, used):
    if len(numbers) == 0:
        return ""
    for i in range(9, -1, -1):
        if not used[i]:
            if not inequalities or (inequalities[0] == '>' and i > int(numbers[0])) or (inequalities[0] == '<' and i < int(numbers[0])):
                used[i] = True
                result = str(i) + find_max(inequalities[1:], numbers[1:], used)
                used[i] = False
                return result

# 최솟값을 구하는 함수
def find_min(inequalities, numbers, used):
    if len(numbers) == 0:
        return ""
    for i in range(10):
        if not used[i]:
            if not inequalities or (inequalities[0] == '>' and i > int(numbers[0])) or (inequalities[0] == '<' and i < int(numbers[0])):
                used[i] = True
                result = str(i) + find_min(inequalities[1:], numbers[1:], used)
                used[i] = False
                return result

# 최댓값 및 최솟값 출력
max_number = find_max(inequalities, numbers, used)
min_number = find_min(inequalities, numbers, used)

print(max_number)
print(min_number)
