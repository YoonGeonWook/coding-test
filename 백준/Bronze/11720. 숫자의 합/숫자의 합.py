import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = input()

res = 0
for a in arr:
	res += int(a)
print(res)