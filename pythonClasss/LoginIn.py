#building an accout creation system
#creating a login system
userName = input("Enter your username: ")
password = input("Enter your password: ")
print("Account created successfully")
print("Login to your account")
username2 = input("Enter your username: ")
password2 = input("Enter your password: ")
if userName == username2 and password == password2:
    print("Login successful")