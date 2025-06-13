# Day 3 - Conditional Statements

# User input
age = int(input("Enter your age: "))

# Basic condition
if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote.")

# Extra: Grading system
score = int(input("Enter your score out of 100: "))

if score >= 90:
    print("🏅 Grade: A")
elif score >= 75:
    print("🥈 Grade: B")
elif score >= 60:
    print("🥉 Grade: C")
else:
    print("❌ Grade: Fail")

# Boolean condition
is_raining = input("Is it raining? (yes/no): ").lower()

if is_raining == "yes":
    print("☔ Take an umbrella!")
else:
    print("😎 Enjoy the sunshine!")

