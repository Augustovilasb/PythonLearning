# Importing the random class in Python
import random

# Creating an opening message
print("\nTHE  B L A C K  J A C K  CLUB!")
print("WELCOME TO THE GAME!")
print("RULES: ")
print("1. Who reaches the closest number up to 21: WIN!")
print("2. If you go over 21, you lose instantly!\n")
print("Let's start...")

# Creating a variable 'play_again' sop the while can start the game
play_again = ""

# Here is the while where the player decides if they want keep playing or leave
# Any value different of '2' keeps the player in the game
while play_again != "2":

    # Creating a variable 'rnd_computer' which will store the computer's random card randint(1, 20)
    # Next, creating a variable 'first_rnd_player' which will store the first player random card randint(1, 20)
    # Constant 'LIMIT' used to check later on if the player went over value '21'
    rnd_computer = random.randint(1, 20)
    first_rnd_player = random.randint(1, 20)
    LIMIT = 21

    print("The computer has his number!!")
    print(f"Your first number: {first_rnd_player}\n")
    print("Take your time and think on that...")

    # Creating a variable 'choose' so the while can run the check if the player wants to buy one more card
    choose = ""

    # Where the program asking if the player wants to buy one more card or no.
    # 'Y' to buy more and 'N' not to buy.
    while choose != "y" and choose != "n":
        choose = input("Would you like to buy one more? (y/n): ").lower()

        # An if to check the answer is valid or not, showing an error message and the loop asks again
        if choose != "y" and choose != "n":
            print("\nInvalid option, type 'Y' for 'yes' and 'N' for 'No': ")

    # If the player has chosen to buy one more card
    if choose == "y":

        # creating a variable 'second_rnd_player' which will store the second player random card randint(1, 20)
        second_rnd_player = random.randint(1, 20)
        print(f"\nYour second number: {second_rnd_player}")
        # Sum of both player cards
        total = first_rnd_player + second_rnd_player
        print(f"Your final number: {first_rnd_player} + {second_rnd_player} = {total}")

        # One more IF, just after the sum of both cards, to check if he went over the LIMIT of 21 value.
        # If the total of both cards is higher than the LIMIT, he loses instantly
        if total > LIMIT:
            print("Oh! It was a mistake!")
            print(f"Blasting yourself! Your number is {total}")
            print("LOSER!")

        # Elif the total of both cards is 21 or under the LIMIT, the player still is in the game
        elif total <= LIMIT:
            # Compare the total of player cards with the computer card
            if total > rnd_computer:
                print("You WON!!!")
                print(f"The value {total} beats the value {rnd_computer} from the computer!!!")
            # Compare the total of player cards with the computer card
            elif total < rnd_computer:
                print("You LOSE!!!")
                print(f"The value {rnd_computer} from the computer beats your number {total}!!!")
            else:
                print("IT'S A DRAW!!!")

    # Else of the "if choose == 'Y'".
    # When the player decides not to buy one more card
    # So only the first random card is compared with the computer's card
    else:
        print("\nAs you prefer!")

        # Comparing the first player's card with the computer's card
        # The program doesn't need to check the LIMIT here, one single card is never over 21
        if first_rnd_player > rnd_computer:  # Higher than the computer: player wins
            print("You WON!!!")
            print(f"The value {first_rnd_player} beats the value {rnd_computer} from the computer!!!")
        elif first_rnd_player < rnd_computer: # Lower than the computer: player loses
            print("You LOSE!!!")
            print(f"The value {rnd_computer} from the computer beats your number {first_rnd_player}!!!")
        else:  # Same number: Extra, It's a draw
            print("IT'S A DRAW!!!")
            print(f"Both of you have the number {rnd_computer}!")

    # Also I created a menu, for the player decide if he wants to play again or no
    # Creating a variable 'play_again' so the while can run the menu check
    play_again = ""

    # Here, if the player types anything different from '1' or '2'
    # the loop will ask him to try again and input a valid number.
    while play_again != "1" and play_again != "2":

        # Type '1' to restart the game, or type '2' to leave the game.
        print("\nPlay again?")
        print("1. Yes \n2. Exit")
        play_again = input("Type 1 or 2: ")

        if play_again == "1":  # Starts a new round
            print("\nHere we go!")
        elif play_again == "2":  # Exit the game
            print("\nThank you for playing!")
        else:
            print("Invalid option, please try again.")