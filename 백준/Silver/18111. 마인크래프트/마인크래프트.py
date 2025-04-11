import sys
input = sys.stdin.readline

from collections import Counter

N, M, B = map(int, input().split())
coords = []
# for _ in range(N):
# 	coords = coords + list(map(int, input().split()))
for _ in range(N):
	coords.extend(map(int, input().split()))

# 높이별로 도수 분포 계산
height_counter = Counter(coords)

# 후보 높이 범위:
min_h = min(height_counter)
max_h = max(height_counter)

# 결과 초기값 설정
min_time = float('inf')
best_h = -1

# 가능한 모든 후보 높이에 대해 소요 시간 계산
for h in range(min_h, max_h + 1):
	time = 0
	inventory = B

	for height, count in height_counter.items():
		if height - h > 0:
			# 제거: 2초 추가, 인벤토리에 추가
			time += 2 * (height - h) * count
			inventory += (height - h) * count

		elif height - h < 0:
			# 쌓기: 1초 추가, 인벤토리에서 제거
			time += (h - height) * count
			inventory -= (h - height) * count

	# 인벤토리가 부족한 경우 건너뛰기
	if inventory < 0:
		continue

	# 시간 갱신 + 높이가 더 높을수록 우선하기
	if time < min_time or (time == min_time and h > best_h):
		min_time = time
		best_h = h

print(min_time, best_h)