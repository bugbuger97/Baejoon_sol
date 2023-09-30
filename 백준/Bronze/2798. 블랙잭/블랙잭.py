n, m = map(int,input().split())
card_number = list(map(int,input().split(' ')))
sum = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if card_number[i] + card_number[j] + card_number[k] <= m:        
        sum = max(sum, card_number[i] + card_number[j] + card_number[k])
print(sum)