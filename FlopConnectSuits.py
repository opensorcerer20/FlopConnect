import sys

# NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
ACE_NUMBER = "m"
NUMBERS = "abcdefghijklm"
SUITS = "shdc"
FLOP_HIT_MIN = 3

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

  def getTranslation(self):
    translation = []
    for card in self.cards:
      translation.append(translateCard(card))
    return translation

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

def translateFlop(flop: Flop):
  return translateCard(flop.cards[0]) + translateCard(flop.cards[1]) + translateCard(flop.cards[2])

def translateHand(hand: Hand):
  return translateCard(hand.cards[0]) + translateCard(hand.cards[1])

def translateCard(card: Card):
  return f"{numberToRank(card.number)}{card.suit}"

def makeDeck():
  deck = []
  for number in NUMBERS:
    for suit in SUITS:
      deck.append(Card(number, suit))
  return deck

def makeAllHands(deck: list[Card]):
  hands = []
  uniqueHands = []
  for i in range(0, len(deck)):
    for j in range(0, len(deck)):
      if (i != j):
        hand = Hand(deck[i], deck[j])

        # sort cards eg "2h 2c" should be "2c 2h"
        original_string = [translateCard(hand.cards[0]), translateCard(hand.cards[1])]
        sorted_characters = sorted(original_string)
        sorted_string = "".join(sorted_characters)

        if not sorted_string in uniqueHands:
          uniqueHands.append(sorted_string)
          hands.append(hand)
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

  # for card in cardsAsRanks:
  for card in sortedString:
    cardVal = convertCardNumberToInt(card)
    if card == sortedString[0:1] and card == ACE_NUMBER:
      firstStraightCard = 1
    else:
      firstStraightCard = cardVal

    # if last straight card is beyond high ace, no more straights possible
    if firstStraightCard + 4 > aceVal:
      firstStraightCard = aceVal - 4

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
    if len(common_chars) >= FLOP_HIT_MIN:
      common_chars2 = "".join(sorted(set(common_chars) & set(hand.numbers)))
      if debug:
        print("common_chars2 " + common_chars)
      if len(common_chars2) > 0:
        return True

  return False
def checkFlushes(hand: Hand, flop: Flop):
  debug = False
  handSuited = hand.cards[0].suit == hand.cards[1].suit

  # foreach card in hand
  for suit in hand.suits:
    if (debug):
      print("\nsuit " + str(suit))
      print("flop suits " + str(flop.suits))
      print("test 1 " + str(flop.suits.count(suit) >= FLOP_HIT_MIN - 1))
      print("test 2 " + str(handSuited and flop.suits.count(suit) >= FLOP_HIT_MIN - 2))
    if flop.suits.count(suit) >= FLOP_HIT_MIN - 1 or (handSuited and flop.suits.count(suit) >= FLOP_HIT_MIN - 2):
      return True
  return False

def flopHasDuplicateCard(hand: Hand, flop: Flop):
  handTranslation = hand.getTranslation()
  flopTranslation = "".join(flop.getTranslation())
  return handTranslation[0] in flopTranslation or handTranslation[1] in flopTranslation

# main loop
def main(hand = ""):
  deck = makeDeck()
  hands = makeAllHands(deck)
  #print("num hands " + str(len(hands)))
  # for hand in hands:
    # print(translateHand(hand))
  # hands = [Hand(Card('a', 's'), Card('a', 'h')), Hand(Card('a', 'h'), Card('a', 's'))]
  flops = makeAllFlops(deck)

  """
  test A2o
  test AKs
  test 1010
  """

  # change to true to export flop-by-flop results
  #hands = [Hand(Card('f', 's'), Card('g', 's'))]
  makeSingleHandCsv = False

  # python3 FlopConnectSuits.py >> flopconnect_test.csv
  if makeSingleHandCsv:
    print(f"hand,flop,pair?,{FLOP_HIT_MIN} straight?,{FLOP_HIT_MIN} flush?")
  else:
    print(f"hand,pair+ chance,{FLOP_HIT_MIN} straight chance,{FLOP_HIT_MIN} flush chance")

  for resultSet in range(0, 10):
    handStart = 140 * resultSet
    handLimit = min(len(hands), 140 * (resultSet + 1))
    flopStart = 0

    # flopLimit = 1000 #len(flops)
    if makeSingleHandCsv:
      flopLimit = min(len(flops), 1200)
    else:
      flopLimit = len(flops)

    if handStart <= len(hands):
      for handIndex in range(handStart, min(len(hands) + 1, handLimit)):
      # thisHand = Hand(Card('m', 's'), Card('a', 'h'))
        thisHand = hands[handIndex]
        totals = dict({"flops": 0, "pairs": 0, "straights": 0, "flushes": 0})
        for flopIndex in range(flopStart, flopLimit):
          # thisHand = hands[handIndex]
          thisFlop = flops[flopIndex]
          if not flopHasDuplicateCard(thisHand, thisFlop):
            totals["flops"] += 1
            hasPair = checkPairs(thisHand, thisFlop)
            hasStraight = checkStraights(thisHand, thisFlop)
            hasFlush = checkFlushes(thisHand, thisFlop)
            if hasPair:
              totals["pairs"] += 1
            if hasStraight:
              totals["straights"] += 1
            if hasFlush:
              totals["flushes"] += 1

            if handLimit == 1 and makeSingleHandCsv:
              row = []
              row.append(translateHand(thisHand))
              row.append(translateFlop(thisFlop))
              #status = "Adult" if age >= 18 else "Minor"
              row.append("PAIR" if hasPair else "-")
              row.append("STR" if hasStraight else "-")
              row.append("FLSH" if hasFlush else "-")
              print(",".join(row))

        if not makeSingleHandCsv:
          # print(str(totals))
          # print("hand: " + translateHand(thisHand))
          results = dict({"hand": translateHand(thisHand), "pair_pct": totals["pairs"] / totals["flops"], "straight_pct": totals["straights"] / totals["flops"], "flush_pct": totals["flushes"] / totals["flops"]})
          pairPct = "{:.3f}".format(results["pair_pct"])
          straightPct = "{:.3f}".format(results["straight_pct"])
          flushPct = "{:.3f}".format(results["flush_pct"])
          print(f"{results["hand"]},{pairPct},{straightPct},{flushPct}")
          # print(str({"hand": translateHand(thisHand), "pair_pct": totals["pairs"] / totals["flops"], "straight_pct": totals["straights"] / totals["flops"], "flush_pct": totals["flushes"] / totals["flops"]}))

# command: python3 FlopConnectSuits.py > results.csv
if __name__ == "__main__":
  # main(sys.argv[1])
  main()
