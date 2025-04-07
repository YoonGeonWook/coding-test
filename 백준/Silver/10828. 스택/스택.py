import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stack = []

for _ in range(N):
	line = input().split()
	cmd = line[0]
	
	if len(line) > 1:
		X = int(line[1])

	if cmd == 'push':
		stack.append(X)
	elif cmd == 'pop':
		if stack:
			print(stack.pop())
		else:
			print(-1)
	elif cmd == 'size':
		print(len(stack))
	elif cmd == 'empty':
		if stack:
			print(0)
		else:
			print(1)
	elif cmd == 'top':
		if stack:
			print(stack[-1])
		else:
			print(-1)
