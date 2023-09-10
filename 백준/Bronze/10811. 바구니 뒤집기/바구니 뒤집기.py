if __name__ == '__main__':
  N, M = map(int,input().split())
  result = [i+1 for i in range(N)]
  for i in range(M):
    i,j = list(map(int,input().split()))
    temp = result[i-1:j]
    temp.reverse()
    result[i-1:j] = temp
  print(*result)