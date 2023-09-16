if __name__ == '__main__':
  n = int(input())
  area = 0
  array = [[0 for _ in range(101)] for _ in range(101)]
  for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
      for j in range(y,y+10):
        array[i][j] = 1
  for i in range(len(array)):
    area += sum(array[i])
  print(area)