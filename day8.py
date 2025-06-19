# Day 8 - Tuples and Sets in Python

# --- Tuples ---
print("=== Tuples ===")
colors = ("red", "green", "blue")
print("All colors:", colors)
print("First color:", colors[0])

# Tuples are immutable - this will cause an error if uncommented
# colors[0] = "yellow"

# --- Sets ---
print("\n=== Sets ===")
fruits = {"apple", "banana", "apple", "orange", "banana"}
print("Unique fruits:", fruits)

# Adding and removing elements in a set
fruits.add("grape")
fruits.discard("banana")
print("Updated fruits:", fruits)

# Check membership
if "apple" in fruits:
    print("🍎 Apple is in the set.")
else:
    print("❌ Apple is not in the set.")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nUnion:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)

