from math import log
from random import choice
from os import system
from art import logo

def devloper_display():
  """For displaying both user results"""
  print(f"\nYour final cards : {user_cards}      Final Score : {sum(user_cards)}\nComputer's Final cards : {comp_cards}        Final Score : {sum(comp_cards)}\n")

def check_total(playerName,list):
  """Check if total of card in a list is less than 21 (playName='user' or 'comp')"""
  playerList={'You':'Computer \U0001F641','Computer':"You \U0001f600"}
  if sum(list)>21:
    print(f"{playerName} Busted. {playerName} Total is {sum(list)} which exeeds 21\n{playerList[playerName]} Won")
    return False
  return True

def display_cards():
  """Display Card details"""
  print(f"\nYour cards : {user_cards}      Current Score : {sum(user_cards)}\nComputer's First cards : {comp_cards[0]}\n")

def randm_Pick_and_Append(playerList):
  """ Randomly Picks and append card to a give list """
  pick = choice(cards)
  if pick == 11 and sum(playerList)<=10:
      return playerList.append(11)
  elif pick == 11 and sum(playerList)>10:
    return playerList.append(1)
  else :
    return playerList.append(pick)
    
def compare():
  """Compare black jack and over scenario"""
  if sum(user_cards)>sum(comp_cards):
    print("You Won \U0001f600")
  elif sum(user_cards)==sum(comp_cards):
    print("Match Draw")
  else:
    print("Computer Won \U0001F641")
def check_for_blackjack():
  if sum(user_cards)==21:
    devloper_display()
    print("You won with BlackJack \U0001f600")
    return True
  elif sum(comp_cards)==21:
    devloper_display()
    print("Computer won with BlackJack \U0001F641")
    return True
  elif sum(user_cards)==22:
    devloper_display()
    print("You Lose. You went over \U0001F641")
    return True
  elif sum(comp_cards)==22:
    devloper_display()
    print("You Won. Computer went over \U0001f600")
    return True
  return False

def Black_Jack():  
  global user_cards,comp_cards,cards
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards=[]
  comp_cards=[]
  for _ in range(2):
    user_cards.append(choice(cards))
    comp_cards.append(choice(cards))
  display_cards()
  anotherPick = True
  notBusted = True
 
  #Check for BlackJack
  blackjack_or_Over = check_for_blackjack()
  
  while  anotherPick and notBusted and not blackjack_or_Over:
    if  input("You want to draw another card. Type 'y' for yes or 'n' for pass :")=='n':  #___COMPUTER's Turn___
      while sum(comp_cards)<17:
        randm_Pick_and_Append(comp_cards)
      devloper_display()
      notBusted=check_total("Computer",comp_cards)
      anotherPick = False
  
    else:   #___USER's Turn___
      randm_Pick_and_Append(user_cards)
      display_cards()
      notBusted = check_total("You",user_cards)
      if sum(user_cards)==21:
        anotherPick = False
        
      
  if notBusted and not blackjack_or_Over :
    #Winning Conditions
    compare()

  if input("\nWant to Continue the game. Type 'y' for yes or 'n' for no  :") =='y':
    system('clear')
    print(logo)
    Black_Jack()
  else:
    print("\n----------x Game Over x----------")

if input("Do you want to play game of BlakJack (y/n):") =='y':
  print(logo)
  Black_Jack()


