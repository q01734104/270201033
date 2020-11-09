x=input("Enter an integer:")
a=int(x[-1])
b=0
if len(x)>1:
  b=int(x[-2])
print(a+b)