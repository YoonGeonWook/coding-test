import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def josephus(N, K):
	result = "<"
	queue = deque(range(1, N+1))

	while len(queue) > 1:
		for _ in range(K-1): # K-1번째 까지 맨 뒤로 보내기
			queue.append(queue.popleft())
		# K번째에서 제거하기
		x = queue.popleft()
		result = result + str(x) + ', '
	result = result + str(queue[-1]) + '>'
	return result

N, K = map(int, input().split())
print(josephus(N, K))