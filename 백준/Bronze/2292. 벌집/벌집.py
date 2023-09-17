if __name__ == '__main__':
  n = int(input())
  cnt = 1
  n_range = 1
  for i in range(1,n+1):
    if n_range >=  n:
      print(cnt)
      break
    else:
      n_range = n_range + 6*i
      cnt+=1