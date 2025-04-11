import sys
input = sys.stdin.readline

from collections import defaultdict

def solution(N, fruits):
	count = defaultdict(int) # 각 과일 종류별 개수를 저장할 딕셔너리 (초기값 0)

	# 왼쪽 포인터 (슬라이딩 윈도우의 시작 위치)
	left = 0

	# 만들 수 있는 가장 긴 탕후루 길이 저장 변수
	max_len = 0

	# 오른쪽 포인터를 0부터 N-1까지 이동
	for right in range(N):
		# 현재 과일을 윈도우에 추가 (종류별 개수 증가)
		count[fruits[right]] += 1

		# 윈도우 내 과일 종류가 2개 초과하면 윈도우 크기를 줄여야 함
		while len(count) > 2:
			count[fruits[left]] -= 1 # 왼쪽 포인터의 과일 크기 한 개 축소
			# 만약 해당 과일의 개수가 0이 되는 경우, 해당 종류 제거
			if count[fruits[left]] == 0:
				del count[fruits[left]]
			# left 크기를 한 칸 옮겨서 윈도우 축소
			left += 1

		# 현재 윈도우의 길이를 계산해서 최대길이 갱신
		# 현재 윈도우 길이: right - left + 1
		max_len = max(max_len, right - left + 1)

	return max_len

N = int(input())
fruits = list(map(int, input().split()))

print(solution(N, fruits))