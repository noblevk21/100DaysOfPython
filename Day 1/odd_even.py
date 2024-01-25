n = int(input("Enter a number:"))

if n % 2 == 1:  # n is odd
    print("Weird")
elif 2 <= n <= 5:  # n is even and in the inclusive range of 2 to 5
    print("Not Weird")
elif 6 <= n <= 20:  # n is even and in the inclusive range of 6 to 20
    print("Weird")
else:  # n is even and greater than 20
    print("Not Weird")
