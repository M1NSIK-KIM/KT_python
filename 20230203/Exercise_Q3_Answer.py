def solution(store, customer):
    answer = []
    
    for request in customer:
        answer.append('yes' if request in store else 'no')
    return answer
