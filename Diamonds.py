for m in range(2,11):
 for n in range(1,m):s="".join([str(i)for i in range(1,n+1)]);print(" "*(10-n)+s+s[::-1][1:])
 for n in range(1,m):s="".join([str(i)for i in list(range(1,m-n))[::-1]]);print(" "*(11-m+n)+s[::-1][:-1]+s)
