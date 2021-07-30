d=lambda m:(d(m-1)if i%m else d(m-1)+[m])if m else[]
for i in range(1,101):print(*d(i))
