import sys
for s in sys.argv[1:]:
 if all(chr(j).lower()in s.lower() for j in range(65,91)):print(s)
