import sys
[print(s)for s in sys.argv if set(s.upper().encode())>=set(range(65,91))]
