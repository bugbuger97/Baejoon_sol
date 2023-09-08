def Alarm_settings(h,m) -> str:
  m -= 45
  if m < 0:
    m += 60
    h -= 1
    if h < 0:
      h += 24
      return f'{h} {m}'
    else: 
      return f'{h} {m}'
  else:
    return f'{h} {m}'
if __name__ == '__main__':
  hour,minute = input().split()
  print(Alarm_settings(int(hour),int(minute)))