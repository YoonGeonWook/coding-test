import sys 
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

coord = [tuple(map(int, input().split())) for _ in range(N)]

coord.sort(key=lambda x: (x[0], x[1]))
for x, y in coord:
	print(x, y)