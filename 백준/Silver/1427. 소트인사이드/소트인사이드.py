temp = sorted(list(map(int,input())),reverse = True)
temp = list(map(str,temp))
result= ''
for i in temp:
  result += i
print(int(result))