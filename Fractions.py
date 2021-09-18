import sys, fractions
for a in sys.argv[1:]:f=fractions.Fraction(a);print(f if'/'in f'{f}'else f'{f}/1')
