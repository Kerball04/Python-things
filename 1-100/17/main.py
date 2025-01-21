while True:
    try:    
        num = int(input("Enter a number of any size: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if 1000 - num <= 100:
        print("The number is close to 1000")
    elif 2000 - num <= 100:
        print("The number is close to 2000")
    else:
        print("The number is not close to 1000 or 2000")