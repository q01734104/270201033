a=2
b=6
c=-20

dif=b**2-4*a*c
a="No Solution"
if dif>0:
  a="x1="+str((-b+dif**0.5)/(-2a))+" x2="+str((-b+dif**0.5)/(-2a))
print(a)