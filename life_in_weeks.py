get_age = int(input("Please input your current age in a number format \n"))


life_in_years = 90 - get_age
life_in_months = life_in_years * 12
life_in_weeks = life_in_years * 52
life_in_days = life_in_years * 365 

print(f"You have {life_in_years} years, {life_in_months} months, {life_in_weeks} weeks, {life_in_days} days to live")