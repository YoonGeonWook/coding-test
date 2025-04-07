import sys
input = lambda: sys.stdin.readline().rstrip()

def is_balanced(line):
	stack = []
	for ch in line:
		if ch in '([':
			stack.append(ch)
		elif ch == ')':                       # 오른쪽 괄호가 등장했는데,
			if not stack or stack[-1] != '(': # 스택이 비어있지 않거나, 왼쪽 괄호가 기존에 없다면 no
				return 'no'
			stack.pop()
		elif ch == ']':
			if not stack or stack[-1] != '[': 
				return 'no'
			stack.pop()
	return 'yes' if not stack else 'no'

# 입력
while True:
	line = input()
	if line == ".":
		break
	print(is_balanced(line))