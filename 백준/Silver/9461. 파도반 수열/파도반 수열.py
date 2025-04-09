import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [0] * (100+1)

def solution(N):
	if N==1 or N==2 or N==3:
		return 1
	if dp[N] != 0:
		return dp[N]
	dp[N] = solution(N-2) + solution(N-3)
	return dp[N]

T = int(input())
for _ in range(T):
	N = int(input())
	print(solution(N))