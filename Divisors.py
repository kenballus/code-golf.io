def d(n,m):return[]if m<1else d(n,m-1)+[m]if n%m<1else d(n,m-1)
for i in range(1,101):print(*d(i,i))
