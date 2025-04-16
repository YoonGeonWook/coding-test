import sys
input = sys.stdin.readline

def backtrack(path, used):
	if len(path) == M:
		# 그냥 path 사용 시, path가 바뀔 경우 result 내부의 값도 함께 바뀜
		# path[:]로 path의 복사본을 저장하는 것!
		result.append(path[:]) 
		return


	for i in range(N):
		if not used[i]:
			used[i] = True
			path.append(nums[i])
			backtrack(path, used)
			path.pop()
			used[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
used = [False] * N

result = []
backtrack([], used)
result = sorted(set(tuple(x) for x in result))
for row in result: 
	print(*row)