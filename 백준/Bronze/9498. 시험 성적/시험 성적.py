def Grade(a) -> str:
  if a >= 90:
    return 'A'
  elif a >= 80:
    return 'B'
  elif a >= 70:
    return 'C'
  elif a >= 60:
    return 'D'
  else:
    return 'F'
  
if __name__ == '__main__':
  score = int(input())
  print(Grade(score))