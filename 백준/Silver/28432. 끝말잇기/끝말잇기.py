n = int(input())
word = [" " for _ in range(n+1)]
pos = 0
answer = ""

for i in range(n):
    word[i] = (input())
    if word[i] == "?":
        pos = i

start = word[pos-1][-1]
finish = word[pos+1][0]

m = int(input())
cdd = []

for i in range(m):
    cdd.append(input())

    if pos == n-1:
        if (cdd[i] not in word) & (cdd[i][0] == start):
            answer = cdd[i]
    elif pos == 0:
        if (cdd[i] not in word) & (cdd[i][-1] == finish):
            answer = cdd[i]
    elif (cdd[i] not in word) & (cdd[i][0] == start) & (cdd[i][-1] == finish):
        answer = cdd[i]
    if ((word[0] == "?") & (word[1] == " ")):
        answer = cdd[i]

print(answer)