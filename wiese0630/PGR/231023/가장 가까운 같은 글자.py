def solution(s):
    answer = []
    nums = []
    new_nums = []
    num = len(s)
    
    for idx in range(num):
        if s[idx] not in s[:idx]:
            answer.append(-1)
        else:
            for i in range(idx):
                if s[idx] == s[i]:
                    nums.append(i)
            for n in nums:
                new_nums.append(abs(n-idx))
            answer.append(min(new_nums))
    return answer