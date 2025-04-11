import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

i = 0
answer = 0
cnt = 0

while i < M - 1:
    # 'IOI' 패턴 발견 시
    if S[i:i+3] == 'IOI':
        cnt += 1
        i += 2  # 'IOI'는 두 칸 이동
        # N개 이상 반복되면 P_N 패턴이 되는 것
        if cnt >= N:
            answer += 1
    else:
        # 패턴이 끊기면 초기화
        cnt = 0
        i += 1

print(answer)
