# Q5 Answer

n = input('숫자를 입력하세요. ')

left, right = 0, 0

l, r = int(n[:len(n)//2]), int(n[len(n)//2:])

while l:
    left += l%10
    l //= 10

while r:
    right += r%10
    r //= 10
    
print("LUCKY" if left == right else "READY")
