import sys
input = lambda: sys.stdin.readline().rstrip()

def fizzbuzz(i):
	if i%3==0 and i%5==0:
		return "FizzBuzz"
	elif i%3==0:
		return "Fizz"
	elif i%5==0:
		return "Buzz"
	else:
		return str(i)

# 입력
seq = [input() for _ in range(3)]

for idx, val in enumerate(seq):
	if val.isdigit():
		i = int(val) - idx
		if [fizzbuzz(i), fizzbuzz(i+1), fizzbuzz(i+2)] == seq:
			print(fizzbuzz(i+3))
			break

