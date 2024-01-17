sugar = int(input())

bag_cnt = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  
        bag_cnt += (sugar // 5)  
        print(bag_cnt)
        break
    sugar -= 3  
    bag_cnt += 1  
else :
    print(-1)