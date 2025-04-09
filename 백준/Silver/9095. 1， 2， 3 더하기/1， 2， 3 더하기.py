import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n):
	dp = [0] * (n+1)
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	dp[n] = solution(n-1) + solution(n-2) + solution(n-3)
	return dp[n]

T = int(input())
for _ in range(T):
	n = int(input())
	print(solution(n))