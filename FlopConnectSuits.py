"""
flopconnect: determine how many flops connect with a hand
"""
"""
matching algorithm
- either card matches one on the flop
- at least 3 suited cards out of 5
- at least 3 straight cards out of 5

- generate file of all possible flops
- generate file of all possible hands

input: one hand
- foreach flop
  - call checkNumbers(hand, flop)
    - get all numbers
    - if any pairs AND ONE IN HAND
      - return true
    - order by number
    - if at least 3 in a straight AND ONE IN HAND
      - return true
    - return false
  - if above true
    - return true
  - call checkSuits(hand, flop)
    - get suits
    - if at least 3 matching suits AND ONE IN HAND
      - return true
    - return false
  - if above true
    - return true
  - return false
"""
# NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
NUMBERS = "abcdefghijklm"
SUITS = "wxyz"

# assume 8 hand table
# 16 cards dealt
# 1 card burn
# 2652 starting hands (includes suits)
# 132600 flops
# if file doesnt exist, generate file of all possible flops
# flops = flops.txt
# numFlops = len(flops)

class Card:
  def __init__(self, number: str, suit: str):
    if number not in NUMBERS:
      return False
    if suit not in SUITS:
      return False
    self.number = number
    self.suit = suit

class Hand:
  def __init__(self, card1: Card, card2: Card):
    self.cards = [card1, card2]
    self.numbers = str(card1.number) + str(card2.number)
    self.suits = str(card1.suit) + str(card2.suit)

class Flop:
  def __init__(self, card1: Card, card2: Card, card3: Card):
    self.cards = [card1, card2, card3]
    self.numbers = str(card1.number) + str(card2.number) + str(card3.number)
    self.suits = str(card1.suit) + str(card2.suit) + str(card3.suit)

def numberToRank(num):
  if num == "i":
    return "10"
  if num == "j":
    return "J"
  if num == "k":
    return "Q"
  if num == "l":
    return "K"
  if num == "m":
    return "A"
  return str(NUMBERS.index(num) + 2)

def suitToSymbol(suit):
  if suit == "w":
    return "s"
  if suit == "x":
    return "h"
  if suit == "y":
    return "d"
  if suit == "z":
    return "c"

def translateFlop(flop: Flop):
  return translateCard(flop.cards[0]) + translateCard(flop.cards[1]) + translateCard(flop.cards[2])

def translateHand(hand: Hand):
  return translateCard(hand.cards[0]) + translateCard(hand.cards[1])

def translateCard(card: Card):
  return f"{numberToRank(card.number)}{suitToSymbol(card.suit)}"

def makeDeck():
  deck = []
  for number in NUMBERS:
    for suit in SUITS:
      deck.append(Card(number, suit))
  return deck

def makeAllHands(deck: list[Card]):
  hands = []
  for i in range(0, len(deck)):
    for j in range(0, len(deck)):
      if (i != j):
        hands.append(Hand(deck[i], deck[j]))
  return hands

def makeAllFlops(deck: list[Card]):
  flops = []
  for i in range(0, len(deck)):
    for j in range(0, len(deck)):
      for k in range(0, len(deck)):
        if (i != j and i != k and j != k):
          flops.append(Flop(deck[i], deck[j], deck[k]))
  return flops

def checkPairs(hand: Hand, flop: Flop):
  # foreach card in hand
  for number in hand.numbers:
    # print("\nnumber " + str(number))
    # print("\nflop " + str(flop.numbers))
    # print("\ntest " + str(number in flop.numbers))
    if number in flop.numbers:
      return True
  return False

def checkStraights(hand: Hand, flop: Flop):
  # get string of flop numbers with no duplicates
  numberString = "".join(map(str, set(flop.numbers)))

  # return false if both hand numbers are in flop
  if hand.numbers[0] in numberString and hand.numbers[1] in numberString:
    return False

  combinedString = "".join(map(str, set(flop.numbers + hand.numbers)))
  sortedString = "".join(sorted(numberString))
  
  """
  test

  """
  
  # max(0, numbers.pos(card1) - 5)
  # min(len(numbers), numbers.pos(card1) + 5)
  
  #{a}efgh good
  #{a}fghi bad
  #abcd{h} good
  #abcd{i} bad
  
  #{e}ijkl good
  #{e}jklm bad
  #efgh{l} good
  #efgh{m} bad

  return False
  # foreach card in hand
  #for number in hand.numbers:

    # if at least 3 out of 5 straight cards
      # return True
  # return False

def checkFlushes(hand: Hand, flop: Flop):
  # if hand is suited and one on flop, return true
  if hand.cards[0].suit == hand.cards[1].suit:
    return hand.cards[0].suit in flop.suits

  # foreach card in hand
  # for number in hand.numbers:
    # print("\nnumber " + str(number))
    # print("\nflop " + str(flop.numbers))
    # print("\ntest " + str(number in flop.numbers))
  #   if number in flop.numbers:
  #     return True
  return False

# main loop
def main():
  deck = makeDeck()
  # print("Number of cards in deck:", len(deck), "\n")
  # print("First encoded card:", deck[0], "\n")
  # print("First card:", translateCard(deck[0]), "\n")
  # print("Last encoded card:", deck[-1], "\n")
  # print("Last card:", translateCard(deck[-1]), "\n")
  hands = makeAllHands(deck)
  # print(f"Number of hands: {len(hands)}\n")
  # print(f"First encoded hand: {hands[0]}\n")
  print(f"First hand: {translateHand(hands[0])}\n")
  print(f"hand 84: {translateHand(hands[83])}\n")
  # print(f"hand encoded 84: {hands[83]}\n")
  # print(f"hand 84: {translateCard(hands[83].cards[0]) + translateCard(hands[83].cards[1])}\n")
  # print(f"Last encoded hand: {hands[-1]}\n")
  # print(f"Last hand: {translateCard(hands[-1].cards[0]) + translateCard(hands[-1].cards[1])}\n")
  flops = makeAllFlops(deck)
  # print(f"Number of flops: {len(flops)}\n")
  # print(f"First encoded flop: {flops[0]}\n")
  print(f"First flop: {translateFlop(flops[0])}\n")
  # print(f"Flop encoded 84: {flops[83]}\n")
  # print(f"Flop 84: {translateCard(flops[83].cards[0]) + translateCard(flops[83].cards[1]) + translateCard(flops[83].cards[2])}\n")
  # print(f"Last encoded flop: {flops[-1]}\n")
  # print(f"Last flop: {translateCard(flops[-1].cards[0]) + translateCard(flops[-1].cards[1]) + translateCard(flops[-1].cards[2])}\n")

  testHand = hands[0]
  connectedFlops = 0
  
  # @TODO flop MUST NOT have cards in hand
  
  
  # for i in range(0, len(flops)):

  # for flop in flops
    # if checkNumbers(hand, flop) or checkSuits(hand, flop)
      # connectedFlops++

  # connectPercent = connectedFlops / numFlops * 100

  # "hand {hand} connected with {connectPercent}% of flops"

if __name__ == "__main__":
  main()
