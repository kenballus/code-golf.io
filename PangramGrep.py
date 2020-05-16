import sys
for s in sys.argv[1:]:
 fail=1
 for j in range(65,91):
  if chr(j)not in s and chr(j).lower()not in s:f=0
 if f:print(s)
