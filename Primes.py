for j in range(2,98):
 a=1;
 for i in range(2,j):
  if j%i<1:a=0
 if a:print(j)
