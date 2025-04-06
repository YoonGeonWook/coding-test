import sys
input = lambda: sys.stdin.readline().rstrip()

d = {i: [1] + [0]*13 for i in range(15)}
d[0] = list(range(1, 15))
for i in range(1, 15):
	for j in range(1, 14):
		d[i][j] = d[i][j-1] + d[i-1][j]

T = int(input())

for _ in range(T):
	k = int(input())
	n = int(input())
	print(d[k][n-1])
