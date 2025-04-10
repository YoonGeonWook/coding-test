import sys
import heapq
input = sys.stdin.readline


N = int(input())
arr = []

for _ in range(N):
	num = int(input())
	if num == 0:
		if not arr:
			print(0)
		else:
			print(-1 * heapq.heappop(arr))
	heapq.heappush(arr, -1 * num)