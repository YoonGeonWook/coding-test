from collections import Counter

from collections import defaultdict

def solution(friends, gifts):

    gift = defaultdict(lambda: defaultdict(int)) # 사람별 타인에게 선물 준 횟수
    gift_idx = {f: 0 for f in friends} # 선물 지수
    
    for g in gifts:
        a, b = g.split()
        gift[a][b] += 1
        gift_idx[a] += 1
        gift_idx[b] -= 1
    

    gift_list = {f: 0 for f in friends}

    for i in friends:
        for j in friends:
            if i != j:
                if gift[i][j] > gift[j][i]:
                    gift_list[i] +=1
                elif gift[i][j] == gift[j][i]:
                    if gift_idx[i] > gift_idx[j]:
                        gift_list[i] += 1
            
    return max(gift_list.values())


