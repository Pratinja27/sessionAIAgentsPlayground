# while condition is true til excutes
# count=0
# while count<3:
#     print(count)
#     print("hello")
#     count=count+1
    

# actual_passward="admin123"
# password=""

# while password != actual_passward:
#     password=input("enter your password:")
#     print("try again")
    
    




actual_password = "admin123"
password = ""
attempts = 0
max_attempts = 5

while password != actual_password and attempts < max_attempts:
    password = input("Enter your password: ")
    attempts += 1

    if password != actual_password:
        print("Try again")

if password == actual_password:
    print("Access granted ")
else:
    print("Too many attempts")


# waiting for process to complete
# retrying an operation
# continuos /infinte code



values=[10,12,-1,]
for i in values:   # [10, 12, -1, 15]
    print(i)
    if i == -1:
        break


