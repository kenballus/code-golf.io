proc f(x:int):int=
 if x<2:x
 else:f(x-1)+f(x-2)
for i in 0..30:echo f(i)
