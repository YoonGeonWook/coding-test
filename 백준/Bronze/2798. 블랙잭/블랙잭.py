import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

N, M = map(int, input().split())
cards = map(int, input().split())
result = -float('inf')
for comb in combinations(cards, 3):
	if sum(comb) <= M:
		if sum(comb) > result:
			result = sum(comb)
print(result)