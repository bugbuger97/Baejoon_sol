def distanse(x,y,w,h):
  return ((x-w)**2 +(y - h) **2) ** 0.5
x,y,w,h = map(int,input().split())
result = [distanse(x,y,0,0),distanse(x,y,w,0),distanse(x,y,0,h),distanse(x,y,w,h),abs(x-w),abs(y-h),x,y]
print(min(result))