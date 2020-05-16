import sys
for s in sys.argv[1:]:
 f=1
 for j in range(65,91):f&=chr(j)in s or chr(j).lower()in s
 if f:print(s)
