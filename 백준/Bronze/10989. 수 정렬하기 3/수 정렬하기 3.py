import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(10001):
     dic[i] = 0

for i in range(n):
        m = int(input())
        dic[m] += 1

for k, v in dic.items():
    while v != 0:
        print(k)
        v -= 1