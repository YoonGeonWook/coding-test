import sys
input = sys.stdin.readline

from collections import deque
from pprint import pprint

M, N, H = map(int, input().split())

# 창고의 상태를 저장할 3차원 배열 (box[z][y][x])
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# BFS를 위한 큐 선언 및 초기 익은 토마토 위치 삽입
queue = deque()
for z in range(H):
	for y in range(N):
		for x in range(M):
			if box[z][y][x] == 1: # 익은 토마토면 큐에 추가
				queue.append((z, y, x))

# 3차원 탐색 방향 정의
dz = [-1, 1, 0, 0, 0, 0] # 위, 아래
dy = [0, 0, -1, 1, 0, 0] # 앞, 뒤
dx = [0, 0, 0, 0, -1, 1] # 좌, 우

# BFS 시작
while queue:
	z, y, x = queue.popleft()

	for i in range(6):
		nz = z + dz[i]
		ny = y + dy[i]
		nx = x + dx[i]

		# 범위를 벗어나지 않고, 익지 않은 토마토(0)인 경우만
		if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
			if box[nz][ny][nx] == 0:
				# 현재 토마토가 익는 날짜는 이전 토마토 + 1일
				box[nz][ny][nx] = box[z][y][x] + 1
				queue.append((nz, ny, nx))


# 결과 계산
days = 0
for z in range(H):
	for y in range(N):
		for x in range(M):
			# 아직 익지 않은 토마토가 있다면 실패
			if box[z][y][x] == 0:
				print(-1)
				exit(0)
			days = max(days, box[z][y][x]) # 가장 늦게 익은 날짜 갱신

# 초기 익은 토마토가 1이므로 정답은 최댓값 - 1
print(days-1)

