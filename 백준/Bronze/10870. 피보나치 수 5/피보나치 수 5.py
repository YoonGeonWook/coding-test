import sys
def input():
	return sys.stdin.readline().rstrip()
n = int(input())

def fibo(n):
	arr = [-1] * (n+2)
	arr[0] = 0
	arr[1] = 1

	if arr[n] != -1:
		return arr[n]

	arr[n] = fibo(n-1) + fibo(n-2)
	return arr[n]
print(fibo(n))