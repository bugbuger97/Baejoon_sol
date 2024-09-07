num = int(input())
tmp = [0, 1, 1]
def fibo(num):
  global tmp
  if num <= 2:
    return tmp[num]
  else:
    while len(tmp) <= num:
      tmp.append(tmp[-1]+tmp[-2])
    return tmp[-1]
print(fibo(num))