password="abc123"
attempt=input("Enter password: ")
if password == attempt:
  print("Welcome")
elif password=="help":
  print(password[0])
else:
  print("Wrong")