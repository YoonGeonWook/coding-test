import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
result = []

for _ in range(N):
	result.append(int(input()))

for r in sorted(result):
	print(r)