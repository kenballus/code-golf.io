import sys
for s in sys.argv[1:]:
 if all(chr(j)in s.upper()for j in range(65,91)):print(s)
