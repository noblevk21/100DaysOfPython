print("Welcome to Tip Calculator!!")

bill = float(input("What was the total bill?"))
tip = int(input("How much you would like to give ? 10, 12 0r 15 ?"))
people = int(input("How many people to spilt the bill?"))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill/people

final_amount = round(bill_per_person,2)
print(f"Each person to be paid is ${final_amount}")