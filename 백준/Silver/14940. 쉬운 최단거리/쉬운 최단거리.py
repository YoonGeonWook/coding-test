import sys
input = sys.stdin.readline

from collections import deque

def bfs(dest, graph, dist, N, M):
	queue = deque([dest])
	dist[dest[0]][dest[1]] = 0 # 목표지점에서 시작하므로 거리가 0

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			# 범위 안에 있고, 갈 수 있는 땅이고, 아직 방문 안했으면
			if 0 <= nx < N and 0 <= ny < M:
				if graph[nx][ny] == 1 and dist[nx][ny] == -1:
					dist[nx][ny] = dist[x][y] + 1
					queue.append((nx, ny))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 결과를 담을 거리 배열 (초기값: -1)
dist = [[-1] * M for _ in range(N)]

# 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 목표지점 좌표 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            dest = (i, j)
            graph[i][j] = 1 # 목표 지점도 갈 수 있는 땅처럼 처리

bfs(dest, graph, dist, N, M)

# 출력 
for i in range(N):
	row = []
	for j in range(M):
		if graph[i][j] == 0:
			row.append(0)
		else:
			row.append(dist[i][j])
	print(' '.join(map(str, row)))