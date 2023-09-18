if __name__ == '__main__':
  while True:
    n = int(input())
    if n == -1:
      break
    else: 
      divisor = [1]
      divisor_str = '1 + '
      for i in range(2,n):
        if n % i == 0:
          divisor.append(i)
          divisor_str += f'{i} + '
      if sum(divisor) == n:
        print(f'{n} = {divisor_str[:-3]}')
      else:
        print(f'{n} is NOT perfect.')