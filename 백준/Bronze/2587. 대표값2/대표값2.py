temp=[]
for i in range(5):
  temp.append(int(input()))
temp=sorted(temp)
print(f'{int(sum(temp)/5)}\n{temp[2]}')