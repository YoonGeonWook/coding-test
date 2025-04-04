import sys
input = lambda: sys.stdin.readline().rstrip()

def hash(L, string):
	M = 1234567891
	result = 0
	for l in range(L):
		result += (ord(string[l])-96) * 31**l
	return result % M

# 입력
L = int(input())
string = input()

# 출력
print(hash(L, string))