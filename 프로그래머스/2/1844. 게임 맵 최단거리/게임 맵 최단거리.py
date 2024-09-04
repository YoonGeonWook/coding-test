from collections import deque

def bfs(maps, x, y, n, m):
    # 상하좌우 지정
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        print(f'(x,y) = {(x,y)}')
        # 현재 위치에서 상하좌우 방향 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나는 경우 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 벽인 경우 무시
            if maps[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny]  = maps[x][y] + 1
                queue.append((nx,ny))
    # 최종 위치가 상대팀 진영이 아닐 시 -1 반환
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]

def solution(maps):
    n, m = len(maps), len(maps[0])   
    return bfs(maps, 0,0, n, m)