while True:
    print("==========Counter Generator==========")
    while True:
        try:
            a = int(input("Enter starting number: "))
            b = int(input("Ebter last number"))
            
        except ValueError:
            print("Invalid input.")
            continue
        break
    
    while True:
        try:
            operation = input("Count Up or down? u/d").lower()
        except ValueError:
            print("invalid input")
            continue
        
        while True:
            if operation == "u":
                while a != b:
                    a = a + 1
                    print(a)
                continue
            elif operation == "d":
                
                while b != a - 1:
                    print(b)
                    b = b - 1
                continue

            else:
                print("invalid input")
                break
    
            status = input("woud you like to conitue? y/n").lower()
            if status == "y":
                continue
            elif status == "n":
                break
