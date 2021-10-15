#This is the wheel of fortune game, I intend to link it to the login_details.txt database file and have a seamless transition from main. It is not yet complete and is missing features, with some variables such as username and balance being temporary to test the game. Additional Note: The UI is not yet finished, and currently looks a little cluttered.- 15/10/21

import random
import numpy as np
import time
import replit

#Menu UI

colour_list = [
    "\033[36;1m", "\033[31;1m", "\033[32;22m", "\033[33;6m", "\033[0;32m",
    "\033[;1m", "\033[;7m", "\033[;4m", "\033[;6m", "\033[36;7m", "\033[1;31m",
    "\033[4;31m"
]

username = "temp" 
balance = 100
#print(colour_list[3])

def UserPortal():
  menu_loop = True
  print(f"Welcome to The Wheel of Fof, {username}!!\n")
  print("__Main Menu__")
  while menu_loop == True:
    c1 = input(f"Press R for Help\nPress P to Continue to the game!\n >>> ").lower()
    if c1 == "r":
      menu_loop = False
      help()
    if c1 == "p":
      menu_loop = False
      break
    else:
      print("Please enter R, or P!")

def help():
  print("\n__Help Section__")
  help_loop = True
  while help_loop == True:
    h1 = input(f"Press R for rules\nPress I for Information\nPress B to return to the Main Menu").lower()
    if h1 == "r":
      print() 
      print("Rules of Wheel of Fof")
      print("There are Five possible Results from each Spin\nThey all have a percentage value of being won, each having respectable payouts\n")
      print("Diamond :: 0.1% Chance :: 100x Payout\nGold    :: 3.9% Chance :: 30x Payout\nPurple  :: 20% Chance  :: 4x Payout\nBlack   :: 38% Chance  :: 2x Payout\nRed     :: 38% Chance  :: 2x Payout\n") #Enter Rules
      print("If you do not bet on the correct result, you lose your bet.\nGood Luck!\n")
      h2 = input(f"Press any button to return to the help section\nPress B to return to the Main Menu\n >>>").lower()
      print()
      if h2 == "b":
        print()
        UserPortal()

    if h1 == "i":
      print() 
      print("Information about Wheel of Fof")
      print("N/A") #Enter Info
      h2 = input(f"Press any button to return to the help section\nPress B to return to the Main Menu\n >>>").lower()
      print()
      if h2 == "b":
        print()
        UserPortal()
    if h1 == "b":
      UserPortal()
      break

#End of Menu UI
 
UserPortal()

#Game Mechanics

board = ["Diamond", "Gold", "Purple", "Black", "Red"]


def game(board, balance):
  print("\n"*2)
  print()
  game_menu = True
  while game_menu == True:
    print(f"\nPlease Place your bet!")
    time.sleep(1)
    betamount = bet_amount(balance)
    betted_colour = bet_colour()
    balance -= betamount
    time.sleep(1)
    print("\n...")
    time.sleep(2)
    print(f"\nBet Successful, you have placed {betamount} on {betted_colour}\nYour Remaining balance is {balance}\n")

    spininit = input("Press F to Spin The wheel of Fof!\nPress B to re-do your bet!").lower()
    if spininit == "f":
        game_menu = False
        print("Wheel Spinning In 3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        
        #clears to reduce UI clutter
        replit.clear()
        
        #Currently Looking into a more efficient way for this to run. 
        #Simulates A spinning wheel in the console.
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.2)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.2)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.5)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.5)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.7)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(0.8)
        fakeresult = spinwheel()
        print(' '.join(fakeresult))
        time.sleep(1.5)
        finalresult = spinwheel()
        print(">>",' '.join(finalresult))
        #                               #

        print(f"\nThe Winning Colour is {' '.join(finalresult)}!!")
        print(f"Your bet was on {betted_colour}")
        if betted_colour == finalresult:
          print("You Won!")
          betamount = winnings_calculator(betamount, finalresult)
          balance += betamount
          print()
          time.sleep(1)
          print(f"{betamount} has been added to your balance!, Congratulations!")
          time.sleep(2)
          print(f"Your Balance is now {balance}")
          exitstate()
        else:
          print("You Lost")
          time.sleep(2)
          exitstate()
      
    if spininit == "b":
      bet()

def spinwheel():
  result = np.random.choice(board, 1, p=[0.001, 0.039, 0.20, 0.38, 0.38])
  return result

def bet_amount(balance):
    bet_menu = True
    while bet_menu == True:
      print("How Much would You like to bet?\n")
      betamount = int(input(">>> "))
      if betamount > balance:
        print("You Do not Have enough funds for this bet!")
      else:
        bet_menu = False
        print("Your Bet amount has been Placed!\n")
        return betamount

def bet_colour():
  print("\nNow please Enter the Colour you would like to bet on!\n")
  time.sleep(1)
  print("Betting List:\n")
  print("Diamond :: 0.1% Chance :: 100x Payout\nGold    :: 3.9% Chance :: 30x Payout\nPurple  :: 20% Chance  :: 4x Payout\nBlack   :: 38% Chance  :: 2x Payout\nRed     :: 38% Chance  :: 2x Payout\n")
  
  colour_menu = True
  while colour_menu == True:

    choose_colour = input("Please Choose a colour to bet on!\n(You Can type The first Letter of the colour.)\n>>>").lower()
    if choose_colour == "d":
      print("You Have placed a bet on Diamond!")
      betted_colour = "Diamond"
      return betted_colour
    if choose_colour == "g":
      print("You Have placed a bet on Gold!")
      betted_colour = "Gold"
      return betted_colour
    if choose_colour == "p":
      print("You Have placed a bet on Purple!")
      betted_colour = "Purple"
      return betted_colour
    if choose_colour == "b":
      print("You Have placed a bet on Black!")
      betted_colour = "Black"
      return betted_colour
    if choose_colour == "r":
      print("You Have placed a bet on Red!")
      betted_colour = "Red"
      return betted_colour
    else: 
      print("Please Choose a Correct Colour!")

def winnings_calculator(betamount, finalresult):
  if finalresult == "Diamond":
    print("YOU WON 100X DIAMOND!!")
    betamount *= 100
  if finalresult == "Gold":
    print("YOU WON 30X GOLD!")
    betamount *= 30
  if finalresult == "Purple":
    print("YOU WON 4X PURPLE")
    betamount *= 4
  if finalresult == "Black":
    print("YOU WON 2X BLACK")
    betamount *= 2
  if finalresult == "Red":
    print("YOU WON 2X RED!!")
    betamount *=2

  return betamount 

def exitstate():
  o1 = input("Would you like to return to the main menu or play again?")
  if o1 == "r":
      UserPortal()
  if o1 == "p":
      game(board, balance)

game(board, balance)

