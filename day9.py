# Day 9 - String Methods and Formatting

name = "Srinadh Reddy"
email = "srinadh@example.com"
greeting = "hello, world!"

# --- String Methods ---
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Title Case:", name.title())
print("Replaced:", name.replace("a", "@"))

print("Starts with 'Srin':", name.startswith("Srin"))
print("Ends with 'Reddy':", name.endswith("Reddy"))
print("Is digit (name):", name.isdigit())
print("Is digit ('123'):", "123".isdigit())

# --- String Formatting ---
age = 25
city = "Hyderabad"

# f-string
print(f"\nMy name is {name}, I'm {age} years old and I live in {city}.")

# format()
print("My name is {}, I'm {} years old and I live in {}.".format(name, age, city))

# % formatting
print("My name is %s, I'm %d years old and I live in %s." % (name, age, city))

