# 스택
# list형태로 뽑아내서 (이 있다면 +1 , )이 있다면 -1
# 합이 -1이 되는 순간 )와 짝이 없기 때문에 무조건 No
# 합이 +1 이상이 돼도 뒤에서 )이 없애줄 가능성이 있기 때문에 계속 진행
# 마지막 합이 +1 이상이어도 남은 것이기 때문에 No
# 오직 0일 때만 YES
a = int(input())
i = 0
sum = 0
while i < a: 
  line = input()
  lines = list(line)
  sum = 0
  for r in lines:
    if r == '(':
      sum += 1
    elif r == ')':
      sum -= 1
    if sum < 0:
      print("NO")
      break
  if sum > 0:
    print("NO")
  elif sum == 0:
    print("YES")
  i += 1