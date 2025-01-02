import sys
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

n = 666
res = 0
while True:
	if '666' in str(n):
		res += 1
	if res == N:
		print(n)
		break
	n += 1

