# 2605
# 입력: 학생수(~100)/ # 줄을 선 차례대로 학생들이 뽑은 번호(0, 자연수, 자신의 순서보다 작은 수) 
#       뽑은 번호 사이에 빈칸이 하나씩 있다
# 출력: 학생들이 처음에 줄을 선 순서대로 1번부터 번호를 매길 때, 
#       학생들이 최종적으로 줄을 선 순서를 번호로 출력한다. 번호 사이 공백 출력

N = int(input())
numbers = [0] + list(map(int, input().split()))
line = [0]

for i in range(1,N+1):
    line.append(str(i))
    a = -1
    while a > - i -1 and line[i-numbers[i]] != str(i):
        line[a], line[a-1] = line[a-1], line[a]
        a -= 1
    # print(i, line)
print(' '.join(line[1:]))