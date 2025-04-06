import sys
input = lambda: sys.stdin.readline().rstrip()

def comparison(A, B):
	if A[0] > B[0] and A[1] > B[1]:
		return True
	else:
		return False

N = int(input())
students = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
	rank = 0
	for j in range(N):
		if i==j:
			continue
		if comparison(students[j], students[i]):
			rank += 1
	print(rank+1, end=' ')

print()