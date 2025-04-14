import sys
input = sys.stdin.readline

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

def solution(M, N, num):
	if num%M == 0 and num%N == 0:
		return M, N
	elif num%M == 0:
		return M, num%N
	elif num%N == 0:
		return num%M, N
	else:
		return num%M, num%N

T = int(input())

for _ in range(T):
	M, N, x, y = map(int, input().split())
	L = lcm(M, N)
	k = x
	flag = False

	while k <= L:
		# (k-1) % N + 1이 y와 같을 때가 우리가 찾는 해
		if (k-1) % N + 1 == y:
			print(k)
			flag = True
			break
		k += M

	if not flag:
		print(-1)