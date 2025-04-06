import sys
input = lambda: sys.stdin.readline().rstrip()

import math

N = int(input())
fact = math.factorial(N)

cnt = 0
fact_str = [f for f in str(fact)]

for f in fact_str[::-1]:
	if f == '0':
		cnt += 1
	else: 
		break

print(cnt)