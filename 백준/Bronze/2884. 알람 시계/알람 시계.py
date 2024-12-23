import sys
input = lambda: sys.stdin.readline().rstrip()

H, M = map(int, input().split())
if M < 45:
	M += 15
	H -= 1
else:
	M -= 45

if H < 0:
	H = 23
print(f"{H} {M}")