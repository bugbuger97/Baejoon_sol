def prime_number(n):
  flag = True
  if n == 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

if __name__ == '__main__':
  N = int(input())
  num = input()
  num = list(map(int,num.split(' ')))
  cnt = 0
  for i in num:
    if prime_number(i):
      cnt+=1
  print(cnt)