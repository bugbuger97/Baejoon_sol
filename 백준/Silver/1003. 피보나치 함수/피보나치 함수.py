t = int(input())
for k in range(0,t):
    n = int(input())
    r = [0,0]
    rest1 = [1,0]
    rest2 = [0,1]
    if n == 0:
        r[0]=rest1[0]
        r[1]=rest1[1]
    elif n==1:
        r[0]=rest2[0]
        r[1]=rest2[1]
    else:
        for i in range(2,n+1):
            r[0] = rest1[0] + rest2[0]
            r[1] = rest1[1] + rest2[1]
            if i%2==0:
                rest1[0]=r[0]
                rest1[1]=r[1]
            else:
                rest2[0]=r[0]
                rest2[1]=r[1]
    print(r[0],r[1])