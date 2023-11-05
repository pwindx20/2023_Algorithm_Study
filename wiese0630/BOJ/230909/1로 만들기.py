def cal(num1, num2):
    return([num1*3, num2+1], [num1*2, num2+1], [num1+1, num2+1] ) 

N = int(input())

lst = [[1, 0]]

while True:
    for elem in lst:
        lst.append(cal(elem[0], elem[1]))
        if elem[0] == N:
            print(elem[1])
            break


