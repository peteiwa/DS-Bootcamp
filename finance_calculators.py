# Assume that you have been approached by a small financial company and asked to create
# a program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.

import math


# Allow user to choose which calculation they want to do

print("\n")
print("investment \t - to calculate the amount of interest you'll earn on your investment")
print("bond \t \t - to calculate the amount you'll have to pay on a home loan \n")

calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculation = calculation.lower()
print("\n")

# After lowercasing the user input, the below section checks if the input is a valid entry.
# If the input is not valid, the program asks again for a user input until valid entry is entered.

valid_entries = ["investment", "bond"]

while calculation not in valid_entries:
    calculation = input("Did you enter a typo? Please enter either 'investment' or 'bond' from the menu above to proceed: ")
    calculation = calculation.lower()
else:
    print("You have selected: \t" + calculation + "\n")

# 1. INVESTMENT
# If the user selects "investment":
if calculation == "investment":
    deposit = int(input("How much money are you depositing, in whole £, e.g. enter '1000' for £1000: "))
    interest_rate = int(input("What is your interest rate? E.g. for 8%, enter '8': "))
    interest_rate = interest_rate/100
    years = int(input("For how many years do you plan on investing? Please enter a whole number, e.g. '3' for 3 years: "))
    interest_type = input("Do you want simple or compound interest? Please enter 'simple' or 'compound': ")
    interest_type = interest_type.lower()

    # simple interest rate, A = P(1 + r*t)
    if interest_type == "simple":
        total = deposit * (1 + interest_rate * years)

    # compound interest rate, A = P(1 + r)^t
    elif interest_type == "compound":
        total = deposit * (1 + interest_rate)**years

    # round to nearest £0.0x and display result
    total = round(total,2)
    print("\n")
    print("------------------------------------------------------------")
    print("\n")
    print("At the end of the investment period, your total investment will be worth £" + str(total)) # NEED TO TIDY UP AND FORMAT OUTPUT (e.g. "Your total investment will be worth £1500.00 at the end of the investment period.")
    print("\n")
    print("------------------------------------------------------------")    

# 2. BOND
# If the user selects "bond":
elif calculation == "bond":

    # Ask user to input the present value of the house, e.g. 100000
    house_value = int(input("What is the value of the house? Please enter to nearest £, e.g. £200000: "))

    # and the interest rate
    interest_rate = int(input("What is your interest rate? E.g. for 8%, enter '8': "))
    interest_rate = (interest_rate/100)/12  # calculate monthly interest rate, e.g. for 8% per month this is 0.08

    # and the number of months they plan to take to repay bond, e.g. 120
    months = int(input("How long do you plan on taking to repay the bond, in months? Please enter a whole number, e.g. '120' for 10 years (120 months): "))

    # Calculate how much money the user will have to repay each month and output the answer    
    # Calculate repayment as = (i * P)/(1 - (1 + i)**(-n))
    # i = interest rate, P = current house value, n = no. of months to pay bond over

    repayment = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-months))
    repayment = round(repayment, 2)

    print("\n")
    print("------------------------------------------------------------")
    print("\n")
    print("You will have to pay £" + str(repayment) + " every month for " + str(months) + " months.")
    print("\n")
    print("------------------------------------------------------------")