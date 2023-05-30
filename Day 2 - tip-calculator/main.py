#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill_without_tip = float(input("What was the total bill? $"))

tip = float(input("How much tip would you like to give? 10, 12, or 15? "))

num_people = int(input("How many people to split the bill? "))

total_bill = total_bill_without_tip * (1 + tip / 100)

each_pay = round(total_bill / num_people, 2)

each_pay_formatted = "{:.2f}".format(each_pay)

print(f"Each person should pay: ${each_pay_formatted}")