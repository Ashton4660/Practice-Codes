while True:
    print("==========Counter Generator==========")
    while True:
    
    #Ask for the starting and ending number.
        
        try:
            a = int(input("Enter starting number: "))
            b = int(input("Enter last number: "))
        
        except ValueError:
            print("Invalid input.")
            print()
            continue
    
    
    #Ask for the option eather up ir down.
        
        try:
            operation = input("Count Up or down? u/d: ").lower()
        except ValueError:
            print("invalid input")
            continue
        
    
    #The operation where it prints the results
        while True:
            
            if operation == "d":
            #This will compare 2 variables and keeps adding the number until it meet the condition.    
                while a != b + 1:
                    print(a)
                    a = a + 1
                break
            
            elif operation == "u":
            #This will compare 2 variables and keeps subtracting the number until it meet the condition.     
                while b != a - 1:
                    print(b)
                    b = b - 1
                break

            else:
                print("invalid input")
                break
        print()
        
    
    #Ask the user whether to continue or not.    
        
        status = input("woud you like to conitue? y/n: ").lower()
        if status == "y":
            continue
        elif status == "n":
            print("Program Terminated.")
            break
    
#Breaks the outer loop putting it to the end of the program.    
    break
