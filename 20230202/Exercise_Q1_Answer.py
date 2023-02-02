# Q1 Answer

def solution(a, b):
    l, r = max(a, b), min(a, b)
     
    while l%r != 0:
        l, r = max(r, l-r), min(r, l-r)

    answer = a*b/r
    return int(answer)

c = solution(7,9)
print(c)
