r=range
for m in r(2,11):
 for n in r(1,m):s="".join(map(str,r(1,n+1)));print(" "*(10-n)+s+s[::-1][1:])
 for n in r(1,m):s="".join(map(str,r(1,m-n)))[::-1];print(" "*(11-m+n)+s[::-1][:-1]+s)
