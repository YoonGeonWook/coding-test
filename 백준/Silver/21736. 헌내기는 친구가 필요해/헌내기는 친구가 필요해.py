import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):
	queue = deque([(x, y)])
	visited[x][y] = True

	people = 0

	while queue:
		x, y = queue.popleft()

		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]

			if 0 <= nx < N and 0 <= ny < M:
				if not visited[nx][ny] and coords[nx][ny] != 'X':
					visited[nx][ny] = True
					queue.append((nx, ny))
					if coords[nx][ny] == 'P':
						people += 1
	return people

N, M = map(int, input().split())
coords = [list(input().strip()) for _ in range(N)]

# 방향 벡터: 상/하/좌/우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문 여부
visited = [[False] * M for _ in range(N)]

# 도연이 위치 찾기 및 DFS 시작
for i in range(N):
	for j in range(M):
		if coords[i][j] == 'I':
			start = (i, j)
			break

result = bfs(start[0], start[1])
print(result if result > 0 else 'TT')