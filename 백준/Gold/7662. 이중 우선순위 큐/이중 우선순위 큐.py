import sys
input = sys.stdin.readline

import heapq

T = int(input())

for test_case in range(T):
	k = int(input())
	min_heap = []
	max_heap = []
	visited = [False] * k # 삽입된 원소 id를 기준으로 삭제 여부 추적

	# print(f"\n=== Test case {test_case + 1} ===")
	for i in range(k):
		oper, num = input().split()
		num = int(num)

		# print(f"\n▶ Operation {i+1}: {oper} {num}")
		if oper == 'I':
			heapq.heappush(min_heap, (num, i))
			heapq.heappush(max_heap, (-num, i))
			visited[i] = True

		else: # D 연산
			if num == 1: # 최댓값 삭제
				# 최대 힙이 비어있지 않고, 그 top에 있는 값이 이미 최소 힙에서 삭제된 값이라면
				# 최대 힙에서 그 값을 꺼내 무시한다.
				while max_heap and not visited[max_heap[0][1]]: 
					heapq.heappop(max_heap) # 즉, 이미 최소 힙에서 최솟값으로 삭제된 것을 처리

				if max_heap: # 최대 힙이 비어있지 않으면
					visited[max_heap[0][1]] = False # 최대 힙에서 최댓값 처리된 id 사용 불가 처리
					heapq.heappop(max_heap)
			elif num == -1: # 최솟값 삭제
				# 최소 힙이 비어있지 않고, 그 top에 있는 값이 이미 최대 힙에서 삭제 처리된 값이라면
				# 최소 힙에서 그 값을 꺼내 무시한다.
				while min_heap and not visited[min_heap[0][1]]:
					heapq.heappop(min_heap)

				if min_heap:
					visited[min_heap[0][1]] = False
					heapq.heappop(min_heap)
		# 디버깅 출력
		# print("  min_heap:", heapq.nsmallest(len(min_heap), min_heap))
		# print("  max_heap:", [(-val, idx) for val, idx in heapq.nsmallest(len(max_heap), max_heap)])
		# print("  visited :", visited)

	# 정리: 아직 남아있는 값 찾기
	while min_heap and not visited[min_heap[0][1]]:
		heapq.heappop(min_heap)
	while max_heap and not visited[max_heap[0][1]]:
		heapq.heappop(max_heap)

	# print("\n✔️ Final Result:")
	if not min_heap or not max_heap:
		print("EMPTY")
	else:
		print(-max_heap[0][0], min_heap[0][0])		


