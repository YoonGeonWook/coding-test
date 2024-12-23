import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

while True:
	try:
		H, W, N = map(int, input().split())
		YY = N % H
		
		if YY == 0:
			YY = H
			XX = (N // H)
		else:
			XX = (N // H) + 1
		print(f"{YY}{XX:02d}")
	except:
		break