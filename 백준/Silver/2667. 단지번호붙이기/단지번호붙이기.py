import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(x, y):
	global cnt

	# 범위 내이면서 집이 있는 경우
	if 0 <= x < N and 0 <= y < N and graph[x][y] == 1:
		graph[x][y] = 0 # 방문 처리
		cnt += 1 # 현재 단지의 집 수 증가
		dfs(x-1, y)
		dfs(x, y-1)
		dfs(x+1, y)
		dfs(x, y+1)
		return True
	return False

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]


res = [] # 각 단지의 집 수를 담을 리스트
for i in range(N):
	for j in range(N):
		if graph[i][j] == 1: # 집인 경우에만 dfs 수행 -> 불필요한 재귀를 사전에 차단
			cnt = 0
			dfs(i, j)
			res.append(cnt)

res.sort()
print(len(res)) # 단지 수
for num in res:
	print(num)