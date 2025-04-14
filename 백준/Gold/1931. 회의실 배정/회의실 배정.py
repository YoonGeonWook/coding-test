import sys
input = sys.stdin.readline

N = int(input())
conf_list = [tuple(map(int, input().split())) for _ in range(N)]

# 종료 시간, 시작 시간 기준으로 정렬
conf_list.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in conf_list:
	if start >= last_end_time:
		count += 1
		last_end_time = end
print(count)