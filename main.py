print("Welcome to the tip calculator\n")
totalBill = float(input("What was the total bill?\n"))
tipPercentage = int(input("What percentage would you like to give? 10,12, 15?\n"))
numOfPpl = int(input("How many people to split the bill?\n"))

individualPay = round((totalBill * tipPercentage / 100) / numOfPpl, 2)
individualPayFormatted = "{:.2f}".format(individualPay)
print(f"Each person should pay: ${individualPay}")