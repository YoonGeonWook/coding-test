import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for i in range(N):
	print(" " * (N-(i+1)) + "*" * (i+1))