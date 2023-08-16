num1 = int(input())
num2 = int(input())

fstnum = num2 // 100
scdnum = (num2 % 100)//10
trdnum = num2 % 10
sumV = num1 * fstnum * 100 + num1 * scdnum * 10 + num1 * trdnum

print(num1 * trdnum)
print(num1 * scdnum)
print(num1 * fstnum)
print(sumV)