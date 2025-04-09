import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [0] * 1001
def solution(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	if dp[n] != 0:
		return dp[n]
	dp[n] = solution(n-1) + solution(n-2)
	return dp[n]

n = int(input())
print(solution(n)%10007)