import sys
input = sys.stdin.readline

def perm_wo_repet(path, used):
	if len(path) == M:
		print(*path)
		return

	for i in range(N):
		# 아직 방문하지 않은 숫자에 대해
		if not used[i]:
			used[i] = True
			path.append(nums[i])
			perm_wo_repet(path, used)
			path.pop()
			used[i] = False

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
used = [False] * N
perm_wo_repet([], used)