import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def is_square(x):
	return int(math.isqrt(x)) ** 2 == x

def solve(x):
	# 1. 하나의 제곱수로 표현
	if is_square(x):
		return 1

	# 2. 두 제곱수의 합으로 표현
	for i in range(1, int(math.sqrt(n)) + 1):
		if is_square(n - i*i):
			return 2

	# 3. 세 제곱수의 합으로 표현
	for i in range(1, int(math.sqrt(n)) + 1):
		for j in range(1, int(math.sqrt(n - i*i)) + 1):
			if is_square(n - i*i - j*j):
				return 3

	return 4

n = int(input())
print(solve(n))