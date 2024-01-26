import sys
N = int(sys.stdin.readline())
temp = sorted([int(sys.stdin.readline()) for i in range(N)])
for i in temp:
  print(i)