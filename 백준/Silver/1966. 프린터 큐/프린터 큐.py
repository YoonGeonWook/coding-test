import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def printer_queue(N, M, priorities):
	
	queue = deque((i, p) for i, p in enumerate(priorities))
	order = 0

	while queue:
		idx, priority = queue.popleft()
		if any(priority < other_p for _, other_p in queue):
			queue.append((idx, priority))
		else:
			order += 1
			if idx == M:
				return order

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	priorities = list(map(int, input().split()))
	print(printer_queue(N, M, priorities))

