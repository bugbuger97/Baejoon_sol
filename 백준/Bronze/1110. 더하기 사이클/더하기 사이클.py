a = input()
if len(a) == 1:
  result = "0" + a
else:
  result = a
for i in range(100):
  temp1 = int(result[1])
  temp2 = int(result[0])
  if temp1 + temp2 < 10:
    result = result[1] + str(temp1+temp2)
  else:
    result = result[1] + str((temp1+temp2)%10)
  if int(result) == int(a):
    print(i+1)
    break