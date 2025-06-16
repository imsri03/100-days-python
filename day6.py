# Day 6 - Python Lists, Indexing, and Slicing

# Creating a list of fruits
fruits = ["apple", "banana", "mango", "orange", "grape"]

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First 3 fruits:", fruits[:3])
print("Fruits from 2 to 4:", fruits[1:4])

# Modifying the list
fruits.append("pineapple")
fruits.remove("banana")
print("Updated list of fruits:", fruits)

# Loop through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# Check if an item exists
if "apple" in fruits:
    print("🍎 Apple is in the list!")

