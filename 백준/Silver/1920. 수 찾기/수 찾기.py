import sys 
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = set(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))


for m in M_lst:
	print(1 if m in A else 0)