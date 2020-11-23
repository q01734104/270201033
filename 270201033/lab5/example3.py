n=int(input("Enter number 1: "))
m=int(input("Enter number 2: "))
k=1
c=0
for i in range(len(str(min(n,m)))):
  k*=10
  if n%k==m%k:
    c+=1
print(c)