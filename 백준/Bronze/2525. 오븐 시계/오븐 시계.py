def Cooking_done(h,m,c) -> str:
  m += c
  while m >= 60:
    m -= 60
    h += 1
  if h >= 24:
    h -= 24
    return f'{h} {m}'
  else:
    return f'{h} {m}'
if __name__ == '__main__':
  hour,minute = input().split()
  cooking_time = int(input())
  print(Cooking_done(int(hour),int(minute),cooking_time))