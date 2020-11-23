n=0
for  i in range(int(input("How many integers? "))):
  if int(input("Enter an integer: "))%2==0:
    n+=1
print(100*(n/(i+1)),"%"")