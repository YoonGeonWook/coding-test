import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
	queue = deque([start])
	visited[start] = True

	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			if not visited[neighbor]: # 아직 방문하지 않았다면
				visited[neighbor] = True # 방문 처리
				parent[neighbor] = node # 부모 설정
				queue.append(neighbor)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (N+1)
parent = [0] * (N+1)

bfs(start = 1)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N+1):
	print(parent[i])