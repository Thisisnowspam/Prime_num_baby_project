#i'm assuming you wanted me to find out if the user input was prime or not. If not, I can come back to this

while 1 == 1:
    num = int(input("Enter a number"))
    if num == 2:
        print("that is a prime number")


    if num > 1 & num !=2:
        for y in range(2,5,num):
            if (num % y) == 0 or (num % 3) == 0 :
                print ("that is not a prime number")
                break
            else:
                print ("That's a prime number")
                break
        restart = str(input("would you like to try again? (y/n)")).lower()
    else:
        print("that is not a prime number")
    if restart == ("y"):
        continue
    if restart == ("n"):
        exit()
    else:
        print("not a valid input")
        break