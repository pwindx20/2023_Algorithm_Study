# 입력: s에는 공백으로 구분된 숫자들이 저장. 최댓값 최소값을 찾아
# 출력: 최소값 최대값 형태의 문자열 반환
def solution(s):
    nums = list(map(int,s.split()))
    return ' '.join([str(min(nums)),str(max(nums))])

s = '1 -1 -2 -3 -4'

print(solution(s))