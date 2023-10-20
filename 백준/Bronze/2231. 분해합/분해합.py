N = int(input())
result,temp = [],[]
for i in range(N,0,-1):
  re = i
  for j in range(len(str(i))):
    temp.append(re%10)
    re //= 10
  if sum(temp)+i == N:
    result.append(i)
  temp = []
if len(result)==0: print(0)
else: print(min(result))
