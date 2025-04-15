import sys
input = sys.stdin.readline

from collections import deque

def bfs(board, start, visited):
	queue = deque()
	queue.append(start)
	visited[1] = True

	while queue:
		current_pos, count = queue.popleft()

		if current_pos == 100:
			return count

		for dice in range(1, 7): # 주사위 1~6
			next_pos = current_pos + dice
			if next_pos <= 100 and not visited[board[next_pos]]:
				visited[board[next_pos]] = True
				queue.append((board[next_pos], count + 1))

N, M = map(int, input().split())

board = [i for i in range(101)] # 칸 번호: 1~100

# 사다리
for _ in range(N):
	x, y = list(map(int, input().split()))
	board[x] = y

# 뱀
for _ in range(M):
	u, v = list(map(int, input().split()))
	board[u] = v

visited = [False] * 101

result = bfs(board, (1, 0), visited)
print(result)