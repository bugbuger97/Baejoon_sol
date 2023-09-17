def index(x):
  n = 0
  for i in range(1,x+1):
    n+=i
    if n >= x:
      return i 
  return 1

if __name__ == '__main__':
  x = int(input())
  id = 0
  result = []
  cnt = 0
  Index = index(x)
  temp = (Index,Index+1)
  for i in range(temp[0]):
    id += i
  if temp[1] % 2 != 0:
    for i in range(temp[0]):    
      result.append((id+1+i,f'{1+i}/{temp[0]-i}'))
      if x == result[i][0]:
        print(result[i][1])
        break
  else:
    for i in range(temp[0]):
      result.append((id+1+i,f'{temp[0]-i}/{1+i}'))
      if x == result[i][0]:
        print(result[i][1])
        break