import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import Counter

def mean(arr):
	return round(sum(arr) / len(arr))

def median(arr):
	arr.sort()
	return arr[len(arr)//2]

def mode(arr):
	cnt = Counter(arr)
	max_freq = max(cnt.values())
	modes = [num for num, freq in cnt.items() if freq == max_freq]
	modes.sort()
	mode = modes[0] if len(modes) == 1 else modes[1] # 두번째로 작은값
	return mode

def num_range(arr):
	return max(arr) - min(arr)

N = int(input())
arr = [int(input()) for _ in range(N)]

print(mean(arr))
print(median(arr))
print(mode(arr))
print(num_range(arr))