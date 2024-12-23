import sys
input = lambda: sys.stdin.readline().rstrip()

A = int(input())
B = int(input())
C = int(input())

ABC = str(A*B*C)
for i in range(10):
	cnt = 0
	for j in ABC:
		if str(i) == j:
			cnt += 1
	print(cnt)