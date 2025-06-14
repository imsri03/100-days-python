# Day 4 - Loops in Python

# 1. Print numbers from 1 to 5 using a for loop
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i)

# 2. Sum numbers in a list
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("Total sum:", total)

# 3. Countdown using while loop
countdown = 5
print("Countdown:")
while countdown > 0:
    print(countdown)
    countdown -= 1
print("🎉 Lift-off!")

