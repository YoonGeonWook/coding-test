import sys
input = sys.stdin.readline

def comb_with_repetition(start, path):
	if len(path) == M:
		print(*path)
		return

	for i in range(start, N):
		path.append(nums[i])
		comb_with_repetition(i, path)
		path.pop()

N, M = map(int, input().split())
nums = list(range(1, N+1))
comb_with_repetition(0, [])