print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give ? 10,12 or 15\n"))
people = int(input("How many people to aplit the bill?\n"))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip/people
rounded_bill = round(bill_per_person,2)
print(f"Each person should pay :${rounded_bill} ")
# f is for fstring it means we dont have to concatenate or convert the data type of variables
