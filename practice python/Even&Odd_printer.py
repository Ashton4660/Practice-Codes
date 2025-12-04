#Author: Ashton4660
#Project: A Program That Print Either Even Or Odd


print("========== Even & Odd number printer ==========")

while True:
    
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input, Please try again.")
            continue
    
    
    while True:
        try:
            print("=== Choose an operation ===")
            print("A. Even")
            print("B. Odd")

            operation = input("Choose: ").upper()
            break
        except ValueError:
            print("Invalid Input.")
            continue

            if operation == "A":
                while a != b:
                    if a % 2 == 0:
                        print(a)
                        a = a + 1

            elif operation == "B":
                while a != b:
                    if a % 2 != 0:
                        print(a)
                        a = a + 1

            





            



        