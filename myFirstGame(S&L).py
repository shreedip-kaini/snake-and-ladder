# we need random int (integer)
import random
from termcolor import colored

# create a player1
player1=0
player1_state = False

#create player2
player2=0
player2_state= False

ladders = {
    3:51,
    6:27,
    20:70,
    36:55,
    63:95,
    68:98
}

snakes = {
    25:5,
    34:1,
    47:19,
    65:52,
    87:57,
    91:61,
    99:69
}

def check_for_snakes_and_ladders(cell_value):
    if cell_value in ladders:
        next_cell_value = ladders[cell_value]
        print(colored(f'YOU FOUND A LADDER! You moved up from {cell_value} to {next_cell_value}', 'green'))
        return next_cell_value
    
    if cell_value in snakes:
        next_cell_value = snakes[cell_value]
        print(colored(f'OOPS! A SNAKE!!! You dropped from {cell_value} to {next_cell_value}', 'red'))
        return next_cell_value
              
    return cell_value


print('''WELCOME TO SNAKE & LADDER GAME
Developed by: SHREEDIP KAINI''')

#let's ask for name from player1 #use capital P
Player1= input('''Player 1:
Enter your name: ''')

#let's ask for name from player2 #use capital P
Player2= input('''Player 2: 
Enter your name: ''')


#ask player1 to roll the dice

while player1_state== False or player2_state== False:
    
   if player1==0:
        dice=input("Player1, Do you want to roll the dice? [y/n]: ")

        if dice == "y":
            player1_roll = random.randint(1,6)
            print("You rolled: ", player1_roll)
            if player1_roll==1:
                print(colored(f"The game has started for {Player1}.", "green"))
                player1_state= True
                player1=1
            else:
                print(colored("Try Again! You need to get 1 to enter", "yellow"))
    
    
        else:
            print(colored("You need to roll the dice to play. Enter 'y' to roll.", "yellow"))
      
        #now game started for player1
   else:
        print()
        if player1_state== True and player1<=100:
            print(colored(f'{Player1},', 'magenta'))
            dice1=input("Do you want to roll the dice? [y/n]: ")
            if dice1 == "y":
                player1_rolls = random.randint(1,6)
                print("You rolled: ", player1_rolls)
                player1+=player1_rolls
                print(Player1, "'s score is : ", player1)
                player1 = check_for_snakes_and_ladders(player1)

        else:
            print(colored("You wasted your turn. Enter 'y' to roll.", "yellow"))
        
         #for player2
   if player2==0:
        dice=input("Player2, Do you want to roll the dice? [y/n]: ")
        if dice == "y":
            player2_roll = random.randint(1,6)
            print("You rolled: ", player2_roll)
            if player2_roll==1:
                print(colored(f"The game has started for {Player2}.", "green"))
                player2_state= True
                player2=1
            else:
                print(colored("Try Again! You need to get 1 to enter", "yellow"))
        else:
            print(colored("You need to roll the dice to play. Enter 'y' to roll.", "yellow"))

            #now game started for player2
   
    
   else:
        print()
        if player2_state== True and player2<=100:
            print(colored(f"{Player2},", "magenta"))
            dice1=input("Do you want to roll the dice? [y/n]: ")
            if dice1 == "y":
                player2_rolls = random.randint(1,6)
                print("You rolled: ", player2_rolls)
                player2+=player2_rolls
                print(Player2, "'s score is : ", player2)
                player2 = check_for_snakes_and_ladders(player2)

        else:
            print(colored("You wasted your turn. Enter 'y' to roll.", "yellow"))
    
print()
print() 
print()   
    
#now both players' state is True
#(just a reminder, this game is developed by Shreedip Kaini)

while player1<100 and player2<100:
     #for player 1
   
   print(colored(f"{Player1},", "magenta"))
   dice1=input("Do you want to roll the dice? [y/n]: ")
   if dice1 == "y":
        player1_rolls = random.randint(1,6)
        print("You rolled: ", player1_rolls)
        player1+=player1_rolls
        if player1>100:
            print(f'You can not roll {player1_rolls}. Try Again!')
            player1-=player1_rolls
        print(Player1, "'s score is : ", player1)
        player1 = check_for_snakes_and_ladders(player1)

   else:
        print(colored("You wasted your turn. Enter 'y' to roll.", "yellow"))
        
   print()
   print()
   print()

   if player1==100:
        print(colored(f"Bravo! {Player1} is the WINNER!!", "grey", "on_cyan"))
   
   else:
            #for player 2
        
        print(colored(f"{Player2},", "magenta"))
        dice1=input("Do you want to roll the dice? [y/n]: ")
        if dice1 == "y":
            player2_rolls = random.randint(1,6)
            print("You rolled: ", player2_rolls)
            player2+=player2_rolls
            if player2>100:
                print(f'You can not roll {player2_rolls}. Try Again!')
                player2-=player2_rolls
            print(Player2, "'s score is : ", player2)
            player2 = check_for_snakes_and_ladders(player2)
        else:
                print(colored("You wasted your turn. Enter 'y' to roll.", "yellow")) 
        
        print()
        print()
        print()

   if player2>=100:
       print(colored(f"Bravo! {Player2} is the WINNER!!", "grey", "on_cyan"))        
        
 #someone has reached 100 and winner has been declared

print() 
print()
print("The Game has Ended. Thank you.")
        
        
