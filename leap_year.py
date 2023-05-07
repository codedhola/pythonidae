year = int(input("Input year to check \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"year {year} is a leap year")
        else: 
            print(f"year {year} not a leap year")
    else: 
        print(f"year {year} not a leap year")
else:
    print(f"year {year} not a leap year")
    