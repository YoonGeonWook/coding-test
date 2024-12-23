import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

L, C = list(map(int, input().split()))
arr = input().split()
res = []

def mo_count(comb):
	cnt = 0
	for c in comb:
		if c in "aeiou":
			cnt += 1
	return cnt, L-cnt
for comb in combinations(arr, L):
	comb = ''.join(sorted(comb))
	mo, ja = mo_count(comb)
	if (mo >= 1) and (ja >= 2):
		res.append(comb)

for r in sorted(res):
	print(r)