for j in range(2,98):
 a=1
 for i in range(2,j):a&=j%i>=1
 if a:print(j)
