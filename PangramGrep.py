import sys
for s in sys.argv[1:]:
 if all(chr(j)in s or chr(j).lower()in s for j in range(65,91)):print(s)
