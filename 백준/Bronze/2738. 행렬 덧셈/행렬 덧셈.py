if __name__ == '__main__':
  A = []
  B = []
  N,M = map(int,input().split())
  for i in range(N):
    temp = list(map(int,input().split()))
    A.append(temp)
  for i in range(N):
    temp = list(map(int,input().split()))
    B.append(temp)
  for i in range(N):
    for j in range(M):
      print(A[i][j] + B[i][j],end=' ')
    print()  