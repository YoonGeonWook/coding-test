import sys
input = lambda: sys.stdin.readline().rstrip()

def divisor(num):
	result = []
	for n in range(1, int(num**0.5)+1):
		if num % n == 0:
			result.append(n)
			result.append(num//n)
	return sorted(result)

def gcd(a, b):
	a_div = set(divisor(a))
	b_div = set(divisor(b))
	a_and_b = a_div.intersection(b_div)
	return max(a_and_b)

def lcm(a, b):
	G = gcd(a, b)
	return (a * b) // G

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))