import sys
input = sys.stdin.readline

N = int(input())
before_comp = list(map(int, input().split()))

unique_sorted = sorted(set(before_comp))
mappings = {v: i for i, v in enumerate(unique_sorted)}

result = [mappings[v] for v in before_comp]
for v in before_comp:
	print(mappings[v], end=' ')