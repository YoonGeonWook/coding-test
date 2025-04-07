import sys
input = lambda: sys.stdin.readline().rstrip()

def mean(scores):
	return sum(scores) / len(scores)

def roundup(num):
	if (num - int(num)) >= 0.5:
		return int(num) + 1
	else:
		return int(num)

N = int(input())

if N == 0:
	print(0)
else:
	scores = sorted([int(input()) for _ in range(N)])
	remove_num = roundup(N * 0.15)
	print(roundup(mean(scores[remove_num:len(scores)-remove_num])))
