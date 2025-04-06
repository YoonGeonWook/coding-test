import sys
input = lambda: sys.stdin.readline().rstrip()

# n*(n-1)*...*(n-k+1) / k*...*1
N, K = map(int, input().split())

nom = 1
denom = 1

for _ in range(K):
	nom *= N
	denom *= K
	N -= 1
	K -= 1

print(int(nom/denom))

