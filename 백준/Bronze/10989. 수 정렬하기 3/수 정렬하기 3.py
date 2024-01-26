import sys
N = int(sys.stdin.readline())
temp = [0] * 10001
for i in range(N):
  num = int(sys.stdin.readline())
  temp[num] = temp[num] + 1
for j in range(10001):
  if temp[j] != 0:
    for k in range(temp[j]):
      print(j)