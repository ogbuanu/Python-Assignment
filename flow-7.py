# question number seven
check1 = input("is it raining outside")
g = "y"
b = "n"
for my_check in check1:
    while my_check == g:
        my_check = input("Have umbrella? ")
        if my_check == b:
            print("wait a while")
            break
        elif my_check == g:print("go outside")
        break
    else: print("go outside")