n = int(input())
temp = [i for i in range(n-2,0,-1)]
sum = 0
for i in temp:
  sum += i*(i+1) // 2
print(sum)
print(3)