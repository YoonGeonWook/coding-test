import sys
input = lambda: sys.stdin.readline().rstrip()

def split_sum(num):
	num_list = [num] + [int(n) for n in str(num)]
	return sum(num_list)

N = int(input())
result = []
for num in range(N):
	if split_sum(num) == N:
		result.append(num)

if result:
	print(min(result))
else:
	print(0)