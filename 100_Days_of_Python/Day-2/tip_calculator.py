#Welcome message
print("Welcome to the tip calculator.\n")

#Ask for total bill
bill = input("What was the total bill? ")
bill_as_float = float(bill)


#Add tip to the bill in %
tip = input("How much tip would you like to give? 10, 12, or 15? ")
tip_as_int = int(tip)
tip_as_percent = tip_as_int / 100


#Split the bill between how many people
people = input("How many people to split the bill? ")
people_as_int = int(people)

#total
total_tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + total_tip_amount
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)

# print(round(total, 2))

print(f"Each person should pay: ${final_amount}")
