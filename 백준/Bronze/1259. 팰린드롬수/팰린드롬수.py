import sys
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()

while True:
	a = str(int(input()))
	
	if a == '0':
		break
	else:
		b = a[::-1]
		if a==b:
			print('yes')
		else:
			print('no')