def solution(n, lost, reserve):
    # reserve에 있는 학생이 lost에 있는 경우
    r_distinct = set(reserve) - set(lost)
    l_distinct = set(lost) - set(reserve)

    for i in sorted(r_distinct): # 빠른 번호부터 처리하기 위해 정렬 사용
        if i-1 in l_distinct:
            l_distinct.remove(i-1)
        elif i+1 in l_distinct:
            l_distinct.remove(i+1)
    return n - len(l_distinct)

# def solution(n, lost, reserve):
#     reserve = set(reserve)-set(lost)
#     lost = set(lost)-set(reserve)
    
#     for r in sorted(reserve):
#         if r+1 in lost:
#             lost.remove(r+1)
#         elif r-1 in reserve:
#             lost.remove(r-1)
#     return n-len(lost)