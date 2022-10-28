# David Liddle 10/27/2022
# Assignment 4

# https://github.com/justinmeister/Mario-Level-1
# https://realpython.com/pygame-a-primer/
# https://codereview.stackexchange.com/questions/217222/pokemon-turn-based-battle-python
# https://www.youtube.com/watch?v=HBbzYKMfx5Y

# https://docs.python.org/3/library/random.html
import random, sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999



# Functions to represent dungeon rooms
def room1(goldAmount, visited_room):
    # TODO: In at least two of your rooms, make up a fun story for the player to read. Create a 'story' function which contains
    # text that you will print out, depending on which room the player enters. (1 pt.)
    #
    # HINT: The 'story' should probably only print out when the player has never visited to room before.

    # TODO: Create a function which implements a simple combat system for the game where the player fights monsters. Players and
    # monsters should take turns against one another. Not every room has to have combat in it. (1 pt.)
    #
    # HINT: You can accomplish this any way you want - use your imagination. However, it will have to print out/ take input for
    # whatever you want to have happen.
    #
    # HINT: You should at least have 'player total health'/ 'player current health'/ 'player damage' variables initially created 
    # in the 'main()' function. You can pass these into the room functions, and then into the combat function.
    #
    # HINT: Whatever stats for whatever monsters you want to implement should likely exist inside the 'combat' function.
    #
    # HINT: Your combat function can, itself, call other sub-functions as well.

    # TODO: Create a function which implements a simple 'shop' for the player to pay some amount of gold to restore their health.
    # Not every room has to have a shop. (1 pt.)
    #
    # HINT: You can accomplish this any way you want - use your imagination. However, it will have to print out/ take input for
    # whatever you want to have happen.
    #
    # HINT: Perhaps players can also pay gold to upgrade their maximum possible health or their attack power.
    #
    # HINT: Whatever stats for shopping you want to implement should likelyh exist inside the 'shop' function.
    #
    # HINT: Your 'shop' function can, itself, call other sub-functions as well.

    # TODO: Create a function which accepts parameters representing the player's 'goldAmount' value, a 'gold' value representing 
    # the amount of gold that the room contains, and a boolean flag indicating whether the room has been visited or not. 
    #
    # This function will operate in a manner similar to the code below, and should return the new 'goldAmount' value that the 
    # player has after adding the gold from the room to their total 'goldAmount'. It should also mark the 'room visited' boolean 
    # flag as 'True', and return that value as well. When returning, assign the new amount of gold to the 'goldAmount' variable, and
    # assign the 'room visited' return value to the 'visited_room' variable. If the room has already been visited before, print
    # out a string indicating this. 
    #
    # This function should be used in all subsequent room functions. (1 pt.)
    #
    # HINT: If the player's health is less than zero, they shouldn't be able to visit rooms anymore.
    #
    # HINT: Study how the 'visited_room' variable is returned at the bottom of this function, and how it interacts with the 
    # 'visited_roomX' variables in the main() function.
    if visited_room == False:
        gold = 10 # This is the amount of gold the room contains.
    
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    # TODO: Create a function which takes in input for the directions the player can go in the dungeon.
    # This function will control how the player moves around the dungeon.
    # This function should replace the following code below this TODO and before the 'return' statement.
    # This function should be used in all subsequent room functions. 
    # This function should return a valid 'roomChoice' value. (1 pt.)
    #
    # HINT: You can do this any way you want. However, it might be an easy solution to take in arguments that 
    # specify valid directions for the player to move, and which rooms they can move to.
    # For example, arguments for N, S, E, W => 2, -1, 3, -1 might allow the player to move north to room 2, 
    # and east to room 3. The values of -1 indicate that the player cannot move that direction.
    #
    # HINT: If you want to give the player fewer than four directions to go, how would you accomplish this in the command print-out? 
    # There are multiple ways to go about this. You don't have to print all the commands on one line. Perhaps you could print out 
    # each command on a different line, and then have the final prompt for the 'input' function just read "What is our choice?: " 
    # or something like that.
    #
    # HINT: If the player's health is less than zero, they shouldn't be able to move to different rooms anymore.
    direction = input("[n] [s] [e] [w]?: ")
    while direction != "n" and direction != "s" and direction != "e" and direction != "w":
        print("Invalid input...")
        direction = input("[n] [s] [e] [w]?: ")
    
    roomChoice = -1 # HINT: Once this section is encapsulated into a function, it would be wise to have a default roomChoice value outside that function.
    if direction == "n":
        roomChoice = 2
    elif direction == "s":
        roomChoice = 2
    elif direction == "e":
        roomChoice = 2
    elif direction == "w":
        roomChoice = 2
    
    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room

# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room2(goldAmount, visited_room):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = -1
    if direction == "n":
        roomChoice = FINAL_ROOM
    elif direction == "s":
        roomChoice = 1

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room

# Main function
def main():
    # Set to 'True' when the game is over.
    gameOver = False

    # Player status variables/ constants. 
    # HINT: If you have other player variables to use, such as health, damage, etc. add them here.
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False # HINT: Carefully study how these 'visited room' variables are used.
    visited_room2 = False

    print("Welcome to Dungeon Crawl...")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: <Student Name>")
    print("[COM S 127 <section>]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            # TODO: Add at least four (4) additional rooms to the dungeon - creating a new 'room' function for each of them (1 pt.)
            #
            # HINT: This will require planning out the layout of your dungeon so that all the 'rooms' connect together correctly.
            #
            # HINT: Study this code carefully to see how the rooms connect, and which room the player is currently inside.
            #
            # NOTE: The other TODO tasks for this assignment can be found in the 'room1' function above.
            while currentRoom != FINAL_ROOM: # HINT: When implmenting combat, if the player's health is <= 0, this loop should not execute.
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1 = room1(goldAmount, visited_room1)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2 = room2(goldAmount, visited_room2)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
            
            # HINT: If the player's health is > 0 when they escape the dungeon print a message like this one. 
            # Otherwise print a message stating that they perished in the dungeon.
            print()
            print("You have escaped with", goldAmount, "gold from the dungeon!")
            print()

            # Reset player values back to their original state
            # HINT: If you add other player values, you will have to reset them to their original values to restart the game.
            #
            # HINT: You can create 'constants' that you can assign to these variables. Doing so means you will only need to 
            # change the values you want to use in one place if you wish to change them.
            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False
        elif choice == "i": # (**"i" Section Tasks**)
            # TODO: Delete the following 'pass' statement and print out instructions for how to play the game. (1 pt.)
            # NOTE: Please feel free to use your imagination here.
            pass
        elif choice == "q": # (**"q" Section Tasks**)
            # TODO: Delete the following 'pass' statement and set the gameOver variable to be 'True' (0.5 pt.)
            # TODO: Print out a 'goodbye' message to the player. (0.5 pt.)
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()