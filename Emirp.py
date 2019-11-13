def p(n):
 for i in range(2,n):
  if n%i<1:return 0
 return 1
for i in range(999):
 r=int(str(i)[::-1])
 if p(i)and p(r)and i!=r:print(i)
