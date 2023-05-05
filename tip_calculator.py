print("Welcome To the tip Calculator")
bill = int(input("What is the total bill \n"))
tip_percent = int(input("What percentage would you like to give? 10, 12, 15 \n"))
split_number = int(input("What number of people to split the bill \n"))

calculations = (bill * tip_percent / 100 + bill) / split_number

print(f"Each person should pay {calculations}")
