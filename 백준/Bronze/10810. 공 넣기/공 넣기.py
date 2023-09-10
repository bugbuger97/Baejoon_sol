if __name__ == '__main__':
  N, M = map(int,input().split())
  result = [0] * N
  for i in range(M):
    i,j,k = list(map(int,input().split()))
    result[i-1:j] = [k] * (j - i + 1)
  print(*result)