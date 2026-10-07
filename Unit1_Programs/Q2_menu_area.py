# Q2. Menu-driven program to calculate areas and simple interest
# Uses if-else for menu selection

print("----- MENU -----")
print("1. Area of Circle")
print("2. Area of Triangle")
print("3. Area of Square")
print("4. Area of Rectangle")
print("5. Simple Interest")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)
elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)
elif choice == 3:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)
elif choice == 4:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == 5:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)
else:
    print("Invalid choice")

# -------Output (Choice 1)-------
# ----- MENU -----
# 1. Area of Circle
# 2. Area of Triangle
# 3. Area of Square
# 4. Area of Rectangle
# 5. Simple Interest
# Enter your choice: 1
# Enter radius: 7
# Area of Circle = 153.86
