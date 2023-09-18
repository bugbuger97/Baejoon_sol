if __name__ == '__main__':
  try:
    N,K = map(int,input().split())
    divisor = [1]
    for i in range(2,N+1):
      if N % i == 0:
        divisor.append(i)
    print(divisor[K-1])
  except IndexError:
    print(0)