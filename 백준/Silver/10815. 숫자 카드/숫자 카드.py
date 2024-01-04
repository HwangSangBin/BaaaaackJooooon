#  딕셔너리

import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

c = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))

result = {}

for i in b:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for j in d:
    total = result.get(j)
    if total == None:
        print(0, end=" ")
    else:
        print(total, end=" ")
