import sys
for f in sys.argv:
 a=[0]*29;i=k=0
 while k<len(f):
  c=f[k];j=a[i];a[i]+=(c=='+')-(c=='-');i+=c=='>';i-=c=='<';o=1
  if'.'==c:print(chr(j),end="")
  if'['==c:
   if j:a+=[k];o=0
   while o:k+=1;o+=f[k]=='[';o-=f[k]==']'
  if']'==c:
   if j:k=a[-1]
   else:a.pop()
  k+=1
