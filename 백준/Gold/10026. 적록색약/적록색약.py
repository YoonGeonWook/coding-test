import sys
input = sys.stdin.readline

# 최대 재귀 깊이 설정
sys.setrecursionlimit(10000)

def dfs(graph, visited, x, y, color):
	visited[x][y] = 1 # 시작 지점 방문 처리

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
	
		# 범위 내에 있고, 방문한 적이 없고, 같은 색상인 경우만 처리
		if 0 <= nx < N and 0 <= ny < N:
			if not visited[nx][ny] and graph[nx][ny] == color:
				dfs(graph, visited, nx, ny, color)

def count_regions(graph):
	visited = [[0] * N for _ in range(N)]
	count = 0

	for i in range(N):
		for j in range(N):
			if not visited[i][j]:
				dfs(graph, visited, i, j, graph[i][j])
				count += 1
	return count

N = int(input())
grid = [input().strip() for _ in range(N)]

# 상하좌우 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

red_green_grid = [[c if c != 'G' else 'R' for c in row] for row in grid]

normal_count = count_regions(grid)
red_green_count = count_regions(red_green_grid)
print(normal_count, red_green_count)