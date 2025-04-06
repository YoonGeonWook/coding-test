import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
counts = [0] * 10001 # 0번 인덱스는 사용하지 않음

for _ in range(N):
	num = int(input())
	counts[num] += 1

for i in range(1, 10001):
	if counts[i] > 0:
		for _ in range(counts[i]):
			print(i)