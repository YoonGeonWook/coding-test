import sys
input = lambda: sys.stdin.readline().rstrip()

from pprint import pprint
from collections import deque

def dfs(graph, v, visited):
	visited[v] = True # 현재 노드를 방문 처리
	print(v, end=' ') # 방문 순서 표현

	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]: # 방문하지 않은 인접노드에 대해
			dfs(graph, i, visited) # 방문 처리를 위해 재귀적으로 호출

def bfs(graph, start, visited):
	queue = deque([start]) 
	visited[start] = True # 현재 노드를 방문 처리

	while queue: # 큐가 빌 때까지 반복
		v = queue.popleft()
		print(v, end =' ')

		# 아직 방문하지 않은 인접 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

# 🔥 인접 리스트 정렬
for i in range(1, N + 1):
	graph[i].sort()

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

dfs(graph, V, visited1)
print()
bfs(graph, V, visited2)
print()