age = input("What is your age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remanining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"you have {days_remaining} days, {weeks_remanining} weeks and {months_remaining} months left")