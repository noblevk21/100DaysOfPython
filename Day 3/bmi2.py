height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi <25:
    print(f"Your bmi is {bmi}, you are having a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are having a Over weight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are having a Obese.")
else:
    print(f"Your bmi is {bmi}, you are having a Clinically obese.")