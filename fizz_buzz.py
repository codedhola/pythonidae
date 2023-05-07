for number in range(1, 101): 
    if number % 3 == 0 and number % 5 == 0: 
        print(f"fizzbuss {number}")
    elif number % 3 == 0: 
        print(f"fizz {number}")
    elif number % 5 == 0:
        print(f"buzz {number}")
    else: 
        print(f"{number}")