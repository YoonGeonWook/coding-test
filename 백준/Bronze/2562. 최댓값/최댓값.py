import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
while True:
	try:
		arr.append(int(input()))
	except:
		break
print(max(arr))
idx = -1

for i in range(len(arr)):
	if arr[i] == max(arr):
		print(i+1)
		break