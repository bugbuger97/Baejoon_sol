# 그룹 단어 확인 횟수 만들기
if __name__ == '__main__':
  T = int(input())
  result = 0
  for i in range(T):
    string = input()
    gabage = list()
    flag = True
    for i in range(len(string)):
      if i != len(string)-1:
        if string[i] in gabage:
          flag = False
          break
        elif string[i] != string[i+1]:
          gabage.append(string[i])
        else:
          continue
      else:
        if string[i] in gabage:
          flag = False
    if flag:
      result += 1
  print(result)