def solution(s):
    answer = []
    uniq = []
    for i in range(len(s)):
        if s[i] not in uniq:
            uniq.append(s[i])
            answer.append(-1)
        else:
            rev = s[:i][::-1]
            cnt = 0
            for ch in rev:
                cnt += 1
                if ch == s[i]:
                    answer.append(cnt)
                    break
    return answer

# def solution(s):
#     answer = []
#     dic = dict()
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i
#     return answer