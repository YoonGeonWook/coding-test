import sys
from collections import deque

input = sys.stdin.readline

def DSLR(start, target):
    visited = [False] * 10000
    queue = deque()
    queue.append((start, ""))  # 명령어 문자열도 같이 저장
    visited[start] = True

    while queue:
        current, cmd = queue.popleft()

        if current == target:
            return cmd

        # D
        next_num = (2 * current) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, cmd + 'D'))

        # S
        next_num = 9999 if current == 0 else current - 1
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, cmd + 'S'))

        # L
        next_num = (current % 1000) * 10 + (current // 1000)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, cmd + 'L'))

        # R
        next_num = (current % 10) * 1000 + (current // 10)
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, cmd + 'R'))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(DSLR(A, B))
