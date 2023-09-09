X = int(input()) # Total amount written on receipt
N = int(input()) # Number of types of items purchased listed on the receipt
result = 0
for i in range(N):
  a,b = input().split()
  temp = int(a)*int(b)
  result += temp
if result == X:
  print('Yes')
else:
  print('No')