import math
import random
import sys
import time

# setting up list of turn options
choices = ["Rock", "Paper", "Scissors"]

# introduce player to application
print("Hello there, this is a Rock, Paper, Scissors game called")
print("""       ____             ____            ____            
      |  _ \\ ___       |  _ \\ __ _     / ___|  ___      
 _____| |_) / _ \\ _____| |_) / _` |____\\___ \\ / __|____ 
|_____|  _ < (_) |_____|  __/ (_| |_____|__) | (_|_____|
      |_| \\_\\___/      |_|   \\__,_|    |____/ \\___|     """)

# set up parameters of game
rounds = (int(input(f"\n\nFirst, how many rounds would you like to play? ")))
win_count = 0
player_wins = 0
comp_wins = 0

# check that number of rounds is odd and greater than 0
if (rounds % 2 == 1) and rounds > 0:
    if rounds > 1:
        print(f"\nPerfect, best {math.ceil(rounds/2)} of {rounds} it is.")
    else:
        print("Okay, just one game to win it all")
else:
    while rounds < 0 or rounds % 2 != 1:
        rounds = (int(input("Please enter a valid number of rounds that is an odd number ")))
    if rounds > 1:
        print(f"\nPerfect, best {math.ceil(rounds/2)} of {rounds} it is.")
    else:
        print("Okay, just one game to win it all")


print("Press 1 for Rock, 2 for Paper, 3 for Scissors")

typing_speed = 20  # wpm


# slow typing function for the round preparation (simulate the anticipation of rock, paper, scissors)
def slow_type(t):
    for character in t:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


# check if the "best '#' of 'rounds'" condition was met or not
while win_count < math.ceil(rounds/2):
    slow_type("\nReady? Set... Go!")

    player_turn = (int(input("")))
    comp_turn = random.randint(1, 3)

    print(f"You chose {choices[player_turn - 1]}!")
    print(f"Computer chose {choices[comp_turn - 1]}!")

    if player_turn == comp_turn:
        print("It's a tie")

    # instances where player wins
    if (player_turn == 1 and comp_turn == 3) or (player_turn == 2 and comp_turn == 1) or (player_turn == 3 and comp_turn == 2):
        print("You WIN!")
        win_count += 1
        player_wins += 1

    # instances where player loses
    if (player_turn == 3 and comp_turn == 1) or (player_turn == 1 and comp_turn == 2) or (player_turn == 2 and comp_turn == 3):
        print("You LOST!")
        win_count += 1
        comp_wins += 1


# when the condition is met, announce the winner
if player_wins > comp_wins:
    print("\nThat's game: You WIN!")
    print(f"{player_wins}-{comp_wins}")
else:
    print("\nThat's game: You LOST")
    print(f"{comp_wins}-{player_wins}")

# ask if player would like to play again
