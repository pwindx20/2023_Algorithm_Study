N = int(input())
start = 2
while N != 1:
    while N % start == 0:
        N = N // start
        print(start)
    start += 1