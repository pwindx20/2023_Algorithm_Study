def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result

def solution(number):
    answer = 0
    ans_list = comb(number, 3)
    for elem in ans_list:
        if sum(elem) == 0:
            answer += 1
    return answer