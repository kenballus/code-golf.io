for j in range(2,98):
 if all(j%i for i in range(2,j)):
  print(j)
