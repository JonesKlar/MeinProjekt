def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def main():
    """Simple function to print a greeting and perform addition."""
    print("Hello, welcome to my Python script!")
    print("Welcome to the simple calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()
