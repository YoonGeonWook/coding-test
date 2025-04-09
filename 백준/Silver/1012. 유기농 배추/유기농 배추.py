import sys
input = lambda: sys.stdin.readline().rstrip()

from pprint import pprint

sys.setrecursionlimit(10000)  # 깊은 재귀를 위해 필요

def dfs(x, y):
	# 주어진 범위를 벗어나는 경우에는 즉시 종료
	if x < 0 or x >= N or y < 0 or y >= M:
		return False

	# 현재 노드를 아직 방문하지 않았다면
	if graph[x][y] == 1:
		# 해당 노드를 방문 처리
		graph[x][y] = 0

		# 상하좌우의 위치들도 모두 재귀적으로 호출
		dfs(x-1, y)
		dfs(x, y-1)
		dfs(x+1, y)
		dfs(x, y+1)
		return True
	return False

T = int(input())

for _ in range(T):
	N, M, K = map(int, input().split())
	graph = [[0] * M for _ in range(N)] # N행 M열

	
	# 2차원 리스트의 맵 정보 입력받기
	for _ in range(K):
		a, b = map(int, input().split())
		graph[a][b] = 1

	# 모든 노드(위치)에 대해 방문하기
	result = 0
	for i in range(N):
		for j in range(M):
			# 현재 위치에서 DFS 수행
			if dfs(i, j) == True: # 해당 노드가 처음 방문하는 곳이라면
				result += 1
	print(result)