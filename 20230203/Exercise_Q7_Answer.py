# Q7 Answer

def solution(arr):
    answer = []
    for n in arr:
        if [n] != answer[-1:]:
            answer.append(n)
    return answer
