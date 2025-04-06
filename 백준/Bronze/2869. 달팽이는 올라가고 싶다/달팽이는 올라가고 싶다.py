import sys
input = lambda: sys.stdin.readline().rstrip()

def snail(A, B, V):
	result = (V-B) // (A-B)
	if (V-B) % (A-B) > 0:
		return result + 1
	return result

A, B, V = map(int, input().split())
print(snail(A, B, V))