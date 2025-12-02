#Author: Ashton4660
#Project: Multiplication generator
#Discription: Provive a single table of multiplication of the input of the user.
#


print("========Multiplication table generator========")

while True:

#Ask for th user in put to be mutiply with.
    try:
        num = int(input("Enter First Number: "))
    except ValueError:
        print("Invalid input")



#The operation where the input will be looped 10 times.
    div = 0
    for i in range(1, 11):
        div = div + 1
        print(f"{num} x {div} = {i * num}")

    
    try:
        status = input("Would you like to try again? y/n: ")

        if status == "y" or status == "Y":
            continue
        elif status == "n" or status == "N":
            break
    except ValueError:
        print("Invalid input.")


