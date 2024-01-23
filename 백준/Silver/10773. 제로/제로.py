# 스택
import sys

num_list = []
a = int(sys.stdin.readline())

for i in range(a):
    num = int(sys.stdin.readline())
    if num == 0:
        if num_list == []:
            pass
            # 0을 넣어야되면 중복제거 하고 == [] or [0]으로 하면 될 듯
        else:
            del num_list[-1]
    else:
        num_list.append(num)
print(sum(num_list))