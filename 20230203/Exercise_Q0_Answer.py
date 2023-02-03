## Q0 Answer

N, X = map(int, input().split())  # N, X 를 입력받음

data = list(map(int, input().split())) # 리스트를 입력받음

answer = [x for x in data if x < X]
for a in answer:
    print(a, end=' ')
