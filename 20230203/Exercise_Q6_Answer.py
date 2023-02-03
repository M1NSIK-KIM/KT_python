# Q6 Answer
def solution(arr):
    answer = arr.copy()
    answer.remove(min(answer))
    if len(answer) == 0: answer.append(-1)
    return answer
