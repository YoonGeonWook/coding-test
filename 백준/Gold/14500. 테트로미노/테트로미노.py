import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

tetromino_shapes = [
	# ㅣ자
	[(0,0), (0,1), (0,2), (0,3)],
	[(0,0), (1,0), (2,0), (3,0)],
	# ㅁ자
	[(0,0), (0,1), (1,0), (1,1)],
	# L자
	[(0,0), (1,0), (2,0), (2,1)],
	[(0,0), (0,1), (1,1), (2,1)],
	[(0,0), (0,1), (0,2), (1,0)],
	[(0,0), (0,1), (0,2), (1,2)],
	[(0,0), (1,0), (1,1), (1,2)],
	[(0,2), (1,0), (1,1), (1,2)],
	[(0,0), (1,0), (2,0), (0,1)],
	[(0,0), (1,0), (2,0), (2,-1)],
	# ㄹ자
	[(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,0), (0,1), (-1,1), (-1,2)],
    [(0,0), (1,0), (1,1), (2,1)],
    # ㅜ자
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,1), (1,0), (1,1), (2,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
]	

max_sum = 0

for i in range(N):
	for j in range(M):
		for shape in tetromino_shapes:
			valid = True
			total = 0
			for dx, dy in shape:
				ni = i + dx
				nj = j + dy
				if 0 <= ni < N and 0 <= nj < M:
					total += grid[ni][nj]
				else:
					valid = False
					break # 하나라도 범위 밖이면 더 안 봐도 됨

			if valid:
				max_sum = max(max_sum, total)

print(max_sum)