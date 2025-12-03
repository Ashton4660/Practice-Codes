#Author: Ashton4660
#Project: Multiplication generator
#Discription: Provive a single table of multiplication of the input of the user.
#


print("========Multiplication table generator========")

while True:

#Ask for th user in put to be mutiply with.
    while True:
        try:
            num = int(input("Enter First Number: "))
            break
        except ValueError:
            print("Invalid input")
            continue



#The operation where the input will be looped 10 times.
    div = 0
    for i in range(1, 11):
        div = div + 1
        print(f"{num} x {div} = {i * num}")

    

    while True:
        
        status = input("Would you like to try again? y/n: ").lower()

        if status == "y" :
            break
        elif status == "n":
            print("Exit.")
            break
        else:
            print("Invalid Input, Please enter 'n' or 'y'")

    if status == "n":
        break
        
        
        


