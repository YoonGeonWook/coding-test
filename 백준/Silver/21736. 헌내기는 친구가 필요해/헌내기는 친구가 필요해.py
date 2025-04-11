import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def dfs(x, y):
	global people # 해당 값을 수정해야 하므로 전역변수 지정
	visited[x][y] = True # 현재 위치 방문 처리

	if coords[x][y] == 'P':
		people += 1

	for d in range(4):
		nx = x + dx[d]
		ny = y + dy[d]

		if 0 <= nx < N and 0 <= ny < M:
			if not visited[nx][ny] and coords[nx][ny] != 'X':
				dfs(nx, ny)

N, M = map(int, input().split())
# coords = []
# for _ in range(N):
# 	coords.append(list(input().strip()))
coords = [list(input().strip()) for _ in range(N)]

# 방향 벡터: 상/하/좌/우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문 여부
visited = [[False] * M for _ in range(N)]
people = 0

# 도연이 위치 찾기 및 DFS 시작
for i in range(N):
	for j in range(M):
		if coords[i][j] == 'I':
			dfs(i, j)
			break

print(people if people > 0 else 'TT')