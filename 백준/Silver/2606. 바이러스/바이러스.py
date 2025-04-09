import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(graph, v, visited):
	visited[v] = True

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# 컴퓨터 수와 직접 연결된 컴퓨터 쌍의 수 입력받기
N = int(input())
M = int(input())
# graph 입력받기 (2차원 리스트)
graph = [[] for _ in range(N+1)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (N+1)

dfs(graph, 1, visited)
print(visited.count(True) - 1)