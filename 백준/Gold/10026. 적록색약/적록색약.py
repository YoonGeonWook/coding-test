import sys
input = sys.stdin.readline

from collections import deque

def bfs(graph, visited, x, y):
	queue = deque([(x, y)])
	visited[x][y] = 1 # 시작 지점 방문 처리

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			# 범위 안에 있고, 방문한 적이 없고, 같은 색상인 경우만
			if 0 <= nx < N and 0 <= ny < N:
				if visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
					visited[nx][ny] = 1
					queue.append((nx, ny))

def count_regions(graph):
	visited = [[0] * N for _ in range(N)]
	count = 0

	for i in range(N):
		for j in range(N):
			if not visited[i][j]:
				bfs(graph, visited, i, j)
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