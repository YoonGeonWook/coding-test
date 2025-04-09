import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
times = list(map(int, input().split()))
order = sorted(times)

result = []
wait_time = 0
for i in range(N):
	wait_time += order[i]
	result.append(wait_time)

print(sum(result))