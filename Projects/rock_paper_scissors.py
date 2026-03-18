import random

# Variable / Comment
#Rock - 1
#Scissors - 2
#Paper - 3
run = True
won = 0
lost = 0

# Main loop
while run == True:
    # User choice
    user_input = int(input(f"""
Won: {won}   Lost: {lost}
Can you choose from one of the options by entering a the number:
        1. Rock
        2. Scissors
        3. Paper
        4. Exit

Enter:"""))
    # Bot choice
    bot_choise = random.randint(1,3) # Choses 1, 2, 3
    
    # Exit code
    if user_input == 4:
        exit()
       
    # Convert number to words
    if user_input == 1:
        user = "Rock"
    elif user_input == 2:
        user = "Scissors"
    else:
        user = "Paper"
    
    if bot_choise == 1:
        bot = "Rock"
    elif bot_choise == 2:
        bot = "Scissors"
    else:
        bot = "Paper"
    
    #Compare
    if user_input == bot_choise:
        if user_input == 1:
            choise = "Rock"
        elif user_input == 2:
            choise = "Scissors"
        else:
            choise = "Paper"
        
        print(f"Both players have chosen {choise}")

    if user == "Paper" and bot == "Rock":
        print (f"You won, the bot chose {bot}")
        won = won + 1
    elif user == "Scissors" and bot == "Paper":
        print (f"You won, the bot chose {bot}")
        won = won + 1
    elif user == "Rock" and bot == "Scissors":
        print (f"You won, the bot chose {bot}")
        won = won + 1
    else:
        print (f"You lost, the bot chose {bot}")
        lost = lost + 1
    

