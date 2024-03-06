def factorial(n):
  if n <= 1: 
    return 1
  else:
    return factorial(n-1) * n

if __name__ == "__main__":
  temp = '0'
  cnt=0
  n = int(input())
  for i in str(factorial(n))[::-1]:
    if i != '0':
      break
    cnt+=1
  print(cnt)