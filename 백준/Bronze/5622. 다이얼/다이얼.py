if __name__ == '__main__':
  S = input()
  result = 0
  delay = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
  for i in S:
    for j in delay.keys():
      if i in j:
        result += delay[j]
  print(result)