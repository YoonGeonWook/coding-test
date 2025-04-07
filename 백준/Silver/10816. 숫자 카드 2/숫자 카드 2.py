import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cards = map(int, input().split())
card_cnt = {}

for c in cards:
	if c in card_cnt: # card_cnt 딕셔너리에 키로 이미 존재한다면
		card_cnt[c] += 1
	else:
		card_cnt[c] = 1

M = int(input())
check_nums = map(int, input().split())

for num in check_nums:
	if num in card_cnt:
		print(card_cnt[num], end=' ')
	else:
		print(0, end=' ')
