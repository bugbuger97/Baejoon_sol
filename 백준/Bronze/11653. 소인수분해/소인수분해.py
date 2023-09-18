if __name__ == '__main__':
  N = int(input())
  if N == 1:
    pass
  else:
    prime_num = []
    cnt = 0
    for i in range(2,N+1):
      if N % i == 0:
        prime_num.append(i)
    for i in range(N):
      if N == 1:
        break
      elif N % prime_num[cnt] == 0:
        print(prime_num[cnt])
        N //= prime_num[cnt]
      else:
        cnt+=1