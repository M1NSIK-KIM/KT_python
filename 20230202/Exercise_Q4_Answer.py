# Q4 Answer
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])
print(f"{result}", end='')

for c in data[1:]:
    
    c = int(c)
    
    if c <= 1 or result <= 1:
        s = '+'
        result += c
    else:
        s = 'X'
        result *= c

    print(f" {s} {c}", end='')
    
print(f" = {result}")
