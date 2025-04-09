import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
notepad = {}
for _ in range(N):
	site, password = input().split()
	notepad[site] = password

for _ in range(M):
	site = input()
	print(notepad[site])