# Q0 Answer

def solution(a, b):
    l, r = max(a, b), min(a, b)
     
    while l%r != 0:
        l, r = max(r, l-r), min(r, l-r)

    answer = r
    return answer

c = solution(3,25)
print(c)
