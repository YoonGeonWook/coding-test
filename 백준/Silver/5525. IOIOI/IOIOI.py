import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

P = 'IO' * N + 'I'

cnt = 0
for start_idx in range(M):
	if S[start_idx:start_idx+len(P)] == P:
		cnt += 1
print(cnt)