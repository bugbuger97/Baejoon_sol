if __name__ == '__main__':
  N,B = input().split()
  B = int(B)
  result = 0
  cnt = 0
  dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,
         'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,
         'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
         'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,
         'Y':34,'Z':35}
  for i in range(len(N)-1,-1,-1):
    if N[i].isdigit():
      result += int(N[i]) * (B**cnt)
    elif N[i] in dic.keys():
      result += dic[N[i]] * (B**cnt)
    cnt+=1
  print(result)