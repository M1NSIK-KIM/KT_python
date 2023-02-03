def solution(n, s):
    answer = []
    if s < n: return [-1]
    while n > 1:
        answer.append(s//n)
        s -= s//n
        n -= 1
        answer.append(s)
    answer = sorted(answer)
    return answer
