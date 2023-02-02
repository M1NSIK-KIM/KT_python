# Q2 Answer

N = int(input())

count = 0

n1, n2 = N//10, N%10

while True:
    n1, n2 = n2, (n1+n2)%10
    count += 1
    
    if n1*10+n2 == N: break

print(count)
