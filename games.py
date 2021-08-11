from random import shuffle, randint

def blackjack_runner():
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
  #print(deck)
  return deck

deck = blackjack_runner()
print(deck)

def card_value(deck):
  deck_values = []

  for card in deck:
    if card[:1] in ('J','Q','K','1'):
       # return int(10)
        deck_values.append(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        #return int(card[:1])
        deck_values.append(card[:1])
  return deck_values

deck_values = card_value(deck)
print(deck_values)

#hand(deck)

def hand(deck, deck_values):
    card_a = deck[randint(0, len(deck))]
    if card_a[:0] == "A":
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                #return int(1)
                deck_values.append(1)
            elif num == '11':
                #return int(11)
                deck_values.append(11)
            else:
                num = input("Do you want your ace to be 1 or 11?\n>")  
    
    card_b = deck[randint(0, len(deck))]
    if card_b[:0] == "A":
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                #return int(1)
                deck_values.append(1)
            elif num == '11':
                #return int(11)
                deck_values.append(11)
            else:
                num = input("Do you want your ace to be 1 or 11?\n>")
     
    return card_a, card_b

def valuecalculator(hand):
    card_a = hand[0]
    card_b = hand[1]
    
    value = 0
    value += int(card_a[:1])
    if card_a == "Q" or "K" or "J":
      value += 10
    value += int(card_b[:1])
    if card_b == "Q" or "K" or "J":
      value += 10

    return value

hand = hand(deck, deck_values)
print(hand)
value = valuecalculator(hand)
print(value)

def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck,card):
    return deck.remove(card)

#round = 1

#for round in game:
#  round += 1

  