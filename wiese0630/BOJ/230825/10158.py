import sys
sys.stdin = open('input10158.txt', 'r')

w, h = map(int, input().split())
arr = [[0]*(w+1) for _ in range(h+1)]
p, q = map(int, input().split())
t = int(input())

for move in range(1, t+1):
