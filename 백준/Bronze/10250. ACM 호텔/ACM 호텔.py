def Room_number(H,W,N) -> str:
  matrix = []
  temp = []
  for i in range(W):
    for j in range(H):
      if i+1 < 10:
        temp.append(str(j+1)+'0'+str(i+1))
      else:
        temp.append(str(j+1)+str(i+1))
    matrix+=temp
    temp = []
  return matrix[N-1] 

if __name__ == '__main__':
  T = int(input())
  for i in range(T):
    H,W,N = map(int,input().split()) # H = 층 수, W = 방 개수, N = 몇 번째 손님
    print(Room_number(H,W,N))