import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
seq = [int(input()) for _ in range(N)]
stack = []
result = []
current = 1 # 다음 push할 숫자

for num in seq:
	# 필요한 수가 나올 때까지 push
	while current <= num:
		stack.append(current)
		result.append('+')
		current+=1

	# top이 원하는 수면 pop
	if stack[-1] == num:
		stack.pop()
		result.append('-')
	else:
		print("NO")
		break
else:
	print('\n'.join(result))

