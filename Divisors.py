def d(n,m):
 if m<1:return[]
 if n%m<1:return d(n,m-1)+[str(m)]
 return d(n,m-1)
for i in range(1,101):print(" ".join(d(i,i)))
