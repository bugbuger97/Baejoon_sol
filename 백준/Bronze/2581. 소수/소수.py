def prime_number(n):
  flag = True
  if n == 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

if __name__ == '__main__':
  M = int(input())
  N = int(input())
  result = []
  for i in range(M,N+1):
    if prime_number(i):
      result.append(i)
  if len(result) == 0:
    print(-1)
  else:
    print(sum(result))
    print(min(result))