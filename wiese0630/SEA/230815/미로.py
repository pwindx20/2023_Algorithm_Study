import sys
sys.stdin = open('input4874.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    forth = list(map(int, input().split()))

    ST = []
    for elem in forth:
        if ST.pop() 