# Q4 Answer

def lcm(a, b):  # 최소공배수
    
    if a < b: l, r = b, a
    else: l, r = a, b
        
    while l%r:
        l, r = max(r, l-r), min(r, l-r)

    return a*b//r

def solution(arr):
    answer = arr[0]
    
    for n in arr[1:]:
        answer = lcm(answer, n)
    
    return answer
