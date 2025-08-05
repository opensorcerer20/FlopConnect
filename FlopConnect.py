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
ACE_NUMBER = "m"
NUMBERS = "abcdefghijklm"
SUITS = "sn"

# reduce numbers by only check "matches suit" or "s" and "doesnt match suit" or "n"

class Card:
  def __init__(self, number: str, suit: str):
    if number not in NUMBERS:
      return False
    if suit not in SUITS:
      return False
    self.number = number
    self.suit = suit

class CardGroup:
  def __init__(self, cards: list[Card], numbers: str, suits: str):
    self.cards = cards
    self.numbers = numbers
    self.suits = suits

class Hand(CardGroup):
  def __init__(self, card1: Card, card2: Card):
    self.cards = [card1, card2]
    self.numbers = str(card1.number) + str(card2.number)
    self.suits = str(card1.suit) + str(card2.suit)

class Flop(CardGroup):
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
  if suit == "s":
    return "s"
  if suit == "n":
    return "n"

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

        # TODO rewrite: flop could have As An An, An An An, but not As As An or As As As
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

# translate a-m to 2-14
def convertCardNumberToInt(number: str):
  if len(number) > 1:
    return False

  value = ord(number) - 95

  if value < 2 or value > 14:
    return False

  return value

def checkStraights(hand: Hand, flop: Flop):
  debug = False
  aceVal = convertCardNumberToInt(ACE_NUMBER)

  # get string of flop numbers with no duplicates
  numberString = "".join(map(str, set(flop.numbers)))

  # if both hand cards are on flop, the straight hit does not count
  if hand.numbers[0] in numberString and hand.numbers[1] in numberString:
    return False

  # add hand cards and remove duplicates
  combinedString = "".join(map(str, set(numberString + hand.numbers)))
  sortedString = "".join(sorted(combinedString))
  
  if debug:
    print("\nNEW test")
    print("hand: " + str(hand.numbers))
    print("flop: " + str(flop.numbers))
    print("sortedString: " + sortedString)

  # ace counts as low in straights, prepend as an extra check
  if ACE_NUMBER in sortedString:
    sortedString = ACE_NUMBER + sortedString

  # get straight ranks
  # cardsAsRanks = []
  # for card in sortedString:
    # a is 97 in ASCII, subtract 95 to get "2"
    # cardsAsRanks.append(ord(card) - 95) # convertCardNumberToInt()

  # for card in cardsAsRanks:
  for card in sortedString:
    cardVal = convertCardNumberToInt(card)
    if card == sortedString[0:1] and card == ACE_NUMBER:
      firstStraightCard = 1
    else:
      firstStraightCard = cardVal

    # @TODO this is wrong, if hand has J and board has KQ, it should return true
    # if last straight card is beyond high ace, no more straights possible
    if firstStraightCard + 4 > aceVal:
      return False

    # create string starting from card and going up 5 chars
    if firstStraightCard == 1:
      # ace special case
      straightCheck = "abcdm"
    else:
      straightCheck = card
      for i in range(firstStraightCard + 1 + 95, firstStraightCard + 5 + 95):
        if debug:
          print("i " + str(i))
        straightCheck += chr(i)

    if debug:
      print("straightCheck " + straightCheck)
      print("sortedString " + sortedString)
    common_chars = "".join(sorted(set(straightCheck) & set(sortedString)))
    if debug:
      print("common_chars1 " + common_chars)
    if len(common_chars) >= 3:
      common_chars2 = "".join(sorted(set(common_chars) & set(hand.numbers)))
      if debug:
        print("common_chars2 " + common_chars)
      if len(common_chars2) > 0:
        return True

  return False

def checkFlushes(hand: Hand, flop: Flop):
  # if hand is suited and one on flop, return true
  if hand.cards[0].suit == hand.cards[1].suit:
    return hand.cards[0].suit in flop.suits

  # foreach card in hand
  for suit in hand.suits:
    # print("\nnumber " + str(number))
    # print("\nflop " + str(flop.numbers))
    # print("\ntest " + str(number in flop.numbers))
    if flop.suits.count("s") > 1 and suit in flop.suits:
      return True
  return False

def flopHasDuplicateCard(hand: Hand, flop: Flop):
  return hand.cards[0] in flop.cards or hand.cards[1] in flop.cards

# main loop
def main():
  deck = makeDeck()
  # print("Number of cards in deck:", len(deck), "\n")
  # print("First encoded card:", deck[0], "\n")
  # print("First card:", translateCard(deck[0]), "\n")
  # print("Last encoded card:", deck[-1], "\n")
  # print("Last card:", translateCard(deck[-1]), "\n")
  hands = makeAllHands(deck)
  # print(f"Number of hands: {len(hands)}\n") # 26 * 25 = 650
  # print(f"First encoded hand: {hands[0]}\n")
  print(f"First hand: {translateHand(hands[0])}\n")
  # print(f"hand 16: {translateHand(hands[15])}\n")
  # print(f"Last encoded hand: {hands[-1]}\n")
  # print(f"Last hand: {translateCard(hands[-1].cards[0]) + translateCard(hands[-1].cards[1])}\n")
  flops = makeAllFlops(deck)
  # print(f"Number of flops: {len(flops)}\n") # 26 * 25 * 24 = 15600
  # print(f"First encoded flop: {flops[0]}\n")
  print(f"First flop: {translateFlop(flops[0])}\n")
  # print(f"Flop encoded 84: {flops[83]}\n")
  # print(f"Flop 16: {translateFlop(flops[15])}")
  # print(f"Last encoded flop: {flops[-1]}\n")
  # print(f"Last flop: {translateCard(flops[-1].cards[0]) + translateCard(flops[-1].cards[1]) + translateCard(flops[-1].cards[2])}\n")
  
  print("hand,flop,pair?,straight?,flush?")
  limit = 1
  for handIndex in range(0, limit):
    for flopIndex in range(0, len(flops)):
      thisHand = hands[handIndex]
      thisFlop = flops[flopIndex]
      if not flopHasDuplicateCard(thisHand, thisFlop):
        row = []
        row.append(translateHand(thisHand))
        row.append(translateFlop(thisFlop))
        row.append(str(checkPairs(thisHand, thisFlop)))
        row.append(str(checkStraights(thisHand, thisFlop)))
        row.append(str(checkFlushes(thisHand, thisFlop)))
        print(",".join(row))

if __name__ == "__main__":
  main()
