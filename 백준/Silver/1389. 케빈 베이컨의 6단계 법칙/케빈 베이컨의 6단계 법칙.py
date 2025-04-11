import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
# for _ in range(M):
# 	a, b = list(map(int, input().split()))
# 	graph[a].append(b)
# 	graph[b].append(a)
for _ in range(M):
	graph.append(tuple(map(int, input().split())))

INF = float('inf')
dist = [[INF] * N for _ in range(N)]

for i in range(N):
	dist[i][i] = 0 # 자기 자신과의 거리는 0

for i, j in graph:
	dist[i-1][j-1] = 1
	dist[j-1][i-1] = 1 # 무방향 그래프이기 때문에 이 부분이 중요!


for k in range(N):
	for i in range(N):
		for j in range(N):
			dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 각 사람의 케빈 베이컨 수 계산
min_total = INF
answer = 0

for i in range(N):
	total = sum(dist[i]) # i번째 사람의 케빈 베이컨 수 
	if total < min_total:
		min_total = total
		answer = i
	elif total == min_total and i < answer:
		answer = i

print(answer + 1)
