from random import shuffle, randint

def blackjack_runner(deck):
  suits = ["♥", "♦", "♣", "♠"]
  deck = []
  for suit in suits:
    for card in range(1, 14):
      if card == 1:
        deck.append("A" + suit)
      elif card == 11:
        deck.append("J" + suit)
      elif card == 12:
        deck.append("Q" + suit)
      elif card == 13:
        deck.append("K" + suit)
      else:
        deck.append(str(card) + suit)
  shuffle(deck)
  print(deck)
  print("ey")
  return deck
   
  deck = blackjack_runner()
  print(deck)
  
  #print("You cards are", playercardA, "&", playercardB)
  #print("Your total is", total)

class blackjack_player(object):
  def __init__(self, hand, deck):
    deck = blackjack_runner()
    self.hand = []
    self.value = 0

#  def set_hand(self, hand):
#    hand == deck[0,1]

#  def get_hand(self, hand):
#    return self.hand

#class dealer(blackjack_player):
#  def __init__(self):
#      super().__init__(hand)
#      print(hand)
#      print("dealer")

#class player(blackjack_player):
#  def __init__(self):
#      super().__init__(hand)
#      print(hand)
#      print("player")