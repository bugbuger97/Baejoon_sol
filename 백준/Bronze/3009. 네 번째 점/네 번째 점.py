x_list = []; y_list = []
for i in range(3): x,y = map(int,input().split()); x_list.append(x);y_list.append(y)
x_result = [i for i in set(x_list) if x_list.count(i) == 1]   
y_result = [i for i in set(y_list) if y_list.count(i) == 1]
print(*(x_result+y_result))