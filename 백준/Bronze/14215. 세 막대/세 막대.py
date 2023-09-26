temp = list(map(int,input().split()))
max_val = max(temp)
min_val = min(temp)
temp.remove(max_val); temp.remove(min_val)
remain_element = temp[0]
while remain_element + min_val <= max_val:
  max_val-=1
print(max_val +  min_val + remain_element)