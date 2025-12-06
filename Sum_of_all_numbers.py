print("========== The sum of all Numbers ==========")

while True:
    
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid Input.")
            continue

    total = 0
    i = 1
    print("\n0")
    while i <= num:
        print("+")
        print(i)
        total += i
        i += 1

    print("\nSum =", total)

    while True:
       
        status = input(("Would you like to try again? y/n: ")).lower()
            
        if status == "y" or status == "yes":
            break
        elif status == "n" or status == "no":
            print("\nProgram Terminated.")
            break
        else:
            print("Invalid Input.")
            continue

    if status == "n":
        break
    