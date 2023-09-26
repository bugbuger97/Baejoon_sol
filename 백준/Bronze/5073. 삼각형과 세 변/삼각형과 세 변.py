while True:
  temp = list(map(int,input().split()))
  if len(set(temp)) == 1 and set(temp) == {0}:
    break
  elif len(set(temp)) == 1 and ((temp[0] < temp[1]+temp[2])and(temp[1] < temp[0]+temp[2])and(temp[2] < temp[1]+temp[0])):
    print('Equilateral')
  elif len(set(temp)) == 2 and ((temp[0] < temp[1]+temp[2])and(temp[1] < temp[0]+temp[2])and(temp[2] < temp[1]+temp[0])):
    print('Isosceles')
  elif len(set(temp)) == 3 and ((temp[0] < temp[1]+temp[2])and(temp[1] < temp[0]+temp[2])and(temp[2] < temp[1]+temp[0])):
    print('Scalene')
  else:
    print('Invalid')
  temp = []