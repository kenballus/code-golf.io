for i in range(1,101):
  if i%sum([int(j)for j in str(i)])==0:print(i)
