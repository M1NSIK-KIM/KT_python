# Q6 Answer

def solution(n):
    answer = -1

    for i in range(n):
        if i*i > n: break
        if i*i == n:
            answer = (i+1)**2

    return answer
  
  solution(121)
