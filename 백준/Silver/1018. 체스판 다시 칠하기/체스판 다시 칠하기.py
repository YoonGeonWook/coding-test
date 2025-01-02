import sys
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
	board.append(input())


for i in range(n-7): 
	for j in range(m-7): # 8x8 로 자르기 위함.
		white = 0 # 체스판의 (0,0)이 흰색인 경우
		black = 0 # 체스판의 (0,0)이 검은색인 경우

		for a in range(i, i+8):
			for b in range(j, j+8):
				if (a+b) % 2 == 0: # (0,0)과 같은 색이어야 하는 칸 (짝수 칸)
					if board[a][b] != 'W': # 'B'인 경우
						white += 1
					else:                  # 'W'인 경우
						black += 1
				else: # (0,0)과 다른 색이어야 하는 칸 (홀수 칸)
					if board[a][b] != 'W': # 'B'인 경우
						black += 1
					else: # 'W'인 경우
						white += 1

		result.append(min(white, black))
print(min(result))