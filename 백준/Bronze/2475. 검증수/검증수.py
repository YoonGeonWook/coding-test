import sys
input = lambda: sys.stdin.readline().rstrip()

arr = map(int, input().split())
summ = 0

for i in arr:
	summ += i**2
print(summ % 10)