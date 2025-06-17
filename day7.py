# Day 7 - Python Dictionaries (key-value pairs)

# Creating a dictionary
person = {
    "name": "Srinadh",
    "age": 25,
    "is_coder": True
}

# Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Is a coder?", person["is_coder"])

# Adding and updating values
person["location"] = "India"
person["age"] = 26

# Deleting a key
del person["is_coder"]

# Final dictionary
print("\nUpdated Profile:")
for key, value in person.items():
    print(f"{key}: {value}")

# Check for a key
if "location" in person:
    print("\n📍 Location is specified.")

