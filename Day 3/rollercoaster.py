print("Welcome to the roller coaster")
height = int(input("What is your height:"))
bill = 0

if height>=120:
    print("You can ride")
    age = int(input("What is your age:"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are 12$")

    want_photo=input("Do you want a photo ? Y or N:\n ")
    if want_photo == "Y":
        #add 3$ to the bill
        bill = bill + 3
    input(f"Total amount to be paid is ${bill}")
    
else:
    print("You can't ride")