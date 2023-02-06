def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def product(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")         
print("3.Multiply")
print("4.Divide")
while True:
    choice =int(input("Enter  your choice: "))
    if choice in (1,2,3,4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f'{num1} + {num2} = {sum(num1, num2)}')

        elif choice == 2:
            print(f'{num1} - {num2} = {subtract(num1, num2)}')

        elif choice == 3:
            print(f'{num1} X {num2} = {product(num1, num2)}')

        elif choice == 4:
            print(f'{num1} / {num2} = {divide(num1, num2)}')
        
        
        opt = input("Do you want to continue? (y for yes/n for no): ")
        if opt == "n":
          break
    
    else:
        print("Invalid Input")

print("Done")
