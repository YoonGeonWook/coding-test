import sys
input = lambda: sys.stdin.readline().rstrip()




M = int(input())

S = set()
for _ in range(M):
	operation = input().split()
	if len(operation) > 1:
		oper, num = operation[0], int(operation[1])
	else:
		oper = operation[0]

	if oper == 'add' and num not in S:
		S.add(num)
	elif oper == 'remove' and num in S:
		S.remove(num)
	elif oper == 'check':
		print(1 if num in S else 0)
	elif oper == 'toggle':
		if num in S:
			S.remove(num)
		else:
			S.add(num)
	elif oper == 'all':
		S = set(range(1, 21))
	elif oper == 'empty':
		S = set()