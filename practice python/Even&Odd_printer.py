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
            print("\nInvalid input, Please try again.")
            continue
    
    
    while True:
        try:
            print("=== Choose an operation ===")
            print("A. Even")
            print("B. Odd")

            operation = input("Choose: ").upper()
            break
        
        except ValueError:
            print("\nInvalid Input.")
            continue

    if operation == "A":
        while a != b + 1:
            if a % 2 == 0:
                print(a)
            a = a + 1

    elif operation == "B":
        while a != b + 1:
            if a % 2 != 0:
                print(a)
            a = a + 1
    
    while True:
        try:
            status = input("Would you like to try again? y/n: ").lower()
        except:
            print("\ninvalid input.")
            continue
        if status == "y":
            continue
        elif status == "n":
            print("\nProgram Ended.")
            break
    break

            





            



        