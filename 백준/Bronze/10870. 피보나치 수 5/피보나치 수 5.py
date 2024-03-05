def fibo(n):
  if n < 2:
    return n
  else:
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
  n = int(input())
  print(fibo(n))