import sys
import heapq
input = sys.stdin.readline

def solution(arr, num):
	if num == 0:
		if not arr: # 배열이 비어있으면 0 출력
			print(0)
		else:
			print(heapq.heappop(arr))
	else:
		heapq.heappush(arr, num)

N = int(input())
arr = []
for _ in range(N):
	num = int(input())
	solution(arr, num)