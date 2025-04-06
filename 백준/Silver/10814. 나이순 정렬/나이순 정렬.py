import sys 
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
members = []
for _ in range(N):
	age, name = input().split()
	age = int(age)
	members.append((age, name))

members.sort(key=lambda x: x[0])

for age, name in members:
	print(age, name)
