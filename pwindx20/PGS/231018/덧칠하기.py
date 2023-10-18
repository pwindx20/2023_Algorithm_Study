# 입력: 페인트가 칠해진 길이 n> 1미터 길이의 구역 n개, 페인트를 칠하는 롤러의 길이는 m미터
#       페인트를 다시 칠하기로 결정한 구역 section (오름차순)
#  1<=m<=n<=100000/ 1<=section의 길이<=n
# 출력: 페인트칠 최소횟수
# 다시 칠하기로 정한 구역은 적어도 한번 페인트칠, 롤러로 페인트칠하는 횟수를 최소화
def solution(n, m, section):
    answer = 0
    arr = [1]*n
    for i in section:
        arr[i-1] = 0
    for j in range(n):
        if not arr[j]:
            for k in range(m):
                if j+k<n:
                    arr[j+k]=1
            answer += 1
    return answer


##### 다른사람 풀이###
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer