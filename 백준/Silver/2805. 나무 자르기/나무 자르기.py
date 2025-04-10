import sys
input = sys.stdin.readline

def solution(M, trees):
	# 이진 탐색 범위 설정: 0부터 max(trees)
	start = 0
	end = max(trees)
	result = 0 # 최종 높이 초기화

	# 이진 탐색 시작
	while start <= end:
		mid = (start + end) // 2 # 절단기 높이 후보 지정

		# 현재 높이(mid)에서 잘라서 얻을 수 있는 나무 길이 총합 계산
		total = 0
		for tree in trees:
			if tree > mid:
				total += tree - mid # 자른 만큼 더하기

		# 디버깅 출력 (탐색 상태 추적)
		# print(f"[탐색] start={start}, end={end}, mid={mid}, total={total}")

		# 자른 양이 충분하면 (즉, M 이상이면), 더 높이 자를 수 있는지 확인
		if total >= M:
			result = mid # 가능한 높이로 지정
			start = mid + 1 # 더 높은 높이 탐색
		else:
			end = mid - 1 # 자른 양이 부족하니 더 낮은 높이를 탐색

	return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(M, trees))