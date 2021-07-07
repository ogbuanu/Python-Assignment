# number ten question
#
# name = ""
# print("who are you")
#
# while name == "":
#     Print('')
#     name = input("Enter name")
#     if name != "joe":
#         name = input("Enter name")
#         break
#     else:
#         print("Hello, joe what is the password? (it is a fish)")
#         password = input("Enter password")
#         if password == "swordfish":
#             print("access granted")
#             break
#         else:
#             name = input("Enter name")
#             continue

while True:
    print("who are you")
    name = input("Enter name ")
    if name != "joe":
        continue
    print("hello joe, what is the password? (it is a fish)")
    password = input("What is the password ")
    if password == "swordfish":
        break
print("Access granted")