import random

# Varables
run = True
i = 4

# Main loop
while run == True:

    # Random guise    
    guise = random.randint(1,10)
    print(guise)

    # Loop for guising
    while i != 0:
        # User guise
        user_input = int(input("""
Can you enter a number from 1 to 10, you have 3 chances (0 to leave)
Enter:"""))
        i = i - 1
        if user_input == 0:
            exit()
        elif user_input == guise:
            print (f"You guised it right on guise {4-i}, the number is {guise}")
        elif user_input < guise:
            print ("The guise is too low")
        elif user_input > guise:
            print ("The guise is too high")
        
    
    print (f"The number was {guise}")