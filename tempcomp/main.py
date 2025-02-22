def c_to_f(c):
    f = c * 9/5 + 32
    return f

def f_to_c(f):
    c = (f - 32) * 5/9
    return c

def read_user_choice():
    choice = int(input("Enter your choice here: "))
    return choice

def read_user_temp():
    temperature = float(input("Enter the temperature: "))
    return temperature

def print_converted_temp(temperature):
    print(f"The resulting temperature is {temperature:.2f}")

def print_menu():
    print("Welcome to the Temperature Converter!")
    print("1) Celsius -> Fahrenheit")
    print("2) Fahrenheit -> Celsius")
    print("3) Exit")

def perform_calcs(choice):
    """Performs calculations based on user choice."""
    if choice == 1:
        temperature = read_user_temp()
        fahrenheit = c_to_f(temperature)
        print_converted_temp(fahrenheit)

    elif choice == 2:
        temperature = read_user_temp()
        celsius = f_to_c(temperature)
        print_converted_temp(celsius)

    elif choice == 3:
        print("Exiting...")
        return False  # Properly terminate the loop

    return True  # Continue looping

def test():
    assert c_to_f(24) == 75.2
    assert f_to_c(75.2) == 24
    print("All function tests passed!")

def main():
    """Main function to run the temperature converter."""
    test()

    flag = True
    while flag:
        print_menu()
        choice = read_user_choice()
        flag = perform_calcs(choice)

if __name__ == "__main__":
    main()
