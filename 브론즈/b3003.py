# 킹, 퀸, 룩, 비숍, 나이트, 폰

hint = [1, 1, 2, 2, 2, 8]

DH = list(map(int,input().split()))

answer = []

for i in range(6):
    answer.append(hint[i]-DH[i])

for i in range(6):
    print(answer[i],end = ' ')
    

