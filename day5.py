# Day 5 - Functions in Python

# 1. Greet the user
def greet(name):
    print(f"Hello, {name}! Welcome to Day 5 of Python.")

# 2. Add two numbers
def add(a, b):
    return a + b

# 3. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Run the functions
greet("Srinadh")

result = add(10, 20)
print("10 + 20 =", result)

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"✅ {num} is a prime number.")
else:
    print(f"❌ {num} is not a prime number.")

