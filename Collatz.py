for n in range(1,1001):
 r=0
 while n>1:n=n*3+1if n%2else n//2;r+=1
 print(r)
