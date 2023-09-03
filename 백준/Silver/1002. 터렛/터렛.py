def turret(T) -> list:
  '''
  Create the input layer as a double list and output it.
  '''
  turret = list()
  temp = list()
  for i in range(T):
    x1, y1, r1, x2, y2, r2 = input().split()
    temp = [x1, y1, r1, x2, y2, r2]
    temp = list(map(int,temp))
    turret.append(temp)
  return turret

def result(turret) -> int:
  '''
  Output the number of intersections between circles
  '''
  result = list()
  for i in range(len(turret)):
    d = ((turret[i][0]-turret[i][3])**2 + (turret[i][1]-turret[i][4])**2)**(1/2)
    if d == 0:
      if turret[i][2] == turret[i][5]:
        result.append(-1)
      else:
        result.append(0)
    else:
      if abs(turret[i][2]-turret[i][5]) < d < abs(turret[i][2]+turret[i][5]):
        result.append(2)
      elif abs(turret[i][2]-turret[i][5]) == d or abs(turret[i][2]+turret[i][5]) == d:
        result.append(1)
      elif abs(turret[i][2]-turret[i][5]) > d or abs(turret[i][2]+turret[i][5]) < d:
        result.append(0)
      else:
        result.append(None)
  return result

if __name__ == '__main__':
  T = int(input())
  result = result(turret(T))
  for i in result:
    print(i)