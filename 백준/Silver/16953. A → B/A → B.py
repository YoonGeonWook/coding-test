import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, target):
	queue = deque([start])
	visited[start] = 0 # 시작점 연산 수: 0
	parent[start] = -1

	while queue:
		now = queue.popleft()

		if now == target:
			path = [] # 경로 복원
			while now != -1:
				path.append(now)
				now = parent[now]
			path.reverse()
			return visited[target], path

		for next_node in [now * 10 + 1, now * 2]:
			# 범위 내에 있고, 아직 방문 하지 않은 숫자라면
			if next_node <= target and next_node not in visited:
				visited[next_node] = visited[now] + 1
				parent[next_node] = now
				queue.append(next_node)

	# 탐색이 끝났는데도 target에 도달하지 못한 경우
	return -1, []

A, B = map(int, input().split())

visited = dict()
parent = dict() # 경로 추적용

steps, path = bfs(A, B)
# if steps == -1:
# 	print("❌ 도달 불가능: -1")
# else:
# 	print("✅ 최소 연산 횟수:", steps + 1)
# 	print("🚀 경로:", ' → '.join(map(str, path)))
if steps == -1:
	print(-1)
else:
	print(steps + 1)