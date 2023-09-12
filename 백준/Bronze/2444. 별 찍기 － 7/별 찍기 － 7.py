if __name__ == '__main__': # 1 -> 3 -> 5 -> 7 -> 9
  star = '*'
  space = ' '
  N = int(input())
  count1 = N-1
  count2 = 1
  for i in range(1,N+1):
    print(f'{space*count1}{star*(2*i-1)}')
    count1 -=1
    if count1 < 0:
      count1 = 0
  for i in range(N-1,0,-1):
    print(f'{space*count2}{star*(2*i-1)}')
    count2 += 1