if __name__ == '__main__':
  a = input() # first
  b = input() # second
  c = int(a)*int(b[2]) # third
  d = int(a)*int(b[1]) # fourth
  e = int(a)*int(b[0]) # fifth
  result = c + d*10 + e*100
  print(f'{c}\n{d}\n{e}\n{result}')