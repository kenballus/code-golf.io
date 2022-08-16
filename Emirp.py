p=lambda n:all(n%i for i in range(2,n))
for i in range(992):
 if p(i)and p(r:=int(str(i)[::-1]))and i!=r:print(i)
