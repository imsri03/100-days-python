# Day 10 - Input Validation and Error Handling

# Validate age input (must be a number)
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("❌ Please enter a valid number for age.")

# Divide two numbers with try/except
try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = num1 / num2
    print(f"✅ Result: {num1} / {num2} = {result}")
except ValueError:
    print("❌ Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("❌ You can't divide by zero!")

# Bonus: Custom error message
print("🎉 Thanks for using the input validator!")

