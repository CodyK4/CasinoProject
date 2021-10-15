#This is a both a placeholdrt & an early verison of my blackjack game, it does not currently work, but some of the core features have been successfully integrated. 

from random import shuffle, randint

def blackjack_runner():
  suits = ["♥", "♦", "♣", "♠"]
  deck = []

  for suit in suits:
    for card in range(1, 14):
      if card == 1:
        deck.append("A")
      elif card == 11:
        deck.append("J")
      elif card == 12:
        deck.append("Q")
      elif card == 13:
        deck.append("K")
      else:
        deck.append(card)

  shuffle(deck)
  #print(deck)
  return deck

deck = blackjack_runner()
print(deck)

def hand(deck):
  card_a_value = 0
  card_b_value = 0

  card_a = deck[randint(0, len(deck))]
  print(f"Your first card is:", card_a)
  if card_a == "A":
        num = input("Do you want this to be 1 or 11?\n>")
        while l1:
            if num == '1':
                #return int(1)
                card_a_value += 1
                l1 = False
            elif num == '11':
                #return int(11)
                card_a_value += 11
                l1 = False

  if card_a in ("J", "K", "Q"):
    card_a_value += 10
  else:
    card_a_value = card_a
      
  card_b = deck[randint(0, len(deck))]
  print(f"Your second card is:", card_b)
  if card_b == "A":
        num = input("Do you want this to be 1 or 11?\n>")
        while l2:
            if num == '1':
                #return int(1)
                card_a_value += 1
                l2 = False
            elif num == '11':
                #return int(11)
                card_a_value += 11
                l2 = False
            else:
                num = input("Do you want your ace to be 1 or 11?\n>") 
  if card_b in ("J", "K", "Q"):
    card_b_value += 10
  else:
    card_b_value = card_b

  total_value = card_a_value + card_b_value
  print(f"Your Total Value is", total_value)

hand = hand(deck)
  