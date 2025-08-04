import unittest
from FlopConnect import checkPairs, translateCard, checkStraights, checkFlushes, Hand, Flop, Card

class TestFlopConnect(unittest.TestCase):
    def test_checkPairs(self):
      # @TODO use new classes
      hand = {
          "cards": [{"number": "a", "suit": "x"}, {"number": "b", "suit": "y"}],
          "numbers": "ab",
          "suits": "xy"
      }
      flop = {
          "cards": [{"number": "a", "suit": "z"}, {"number": "d", "suit": "y"}, {"number": "e", "suit": "z"}],
          "numbers": "ade",
          "suits": "zyz"
      }
      
      # Check if first card number in hand matches a card in flop
      result = checkPairs(hand, flop)
      self.assertTrue(result)

      # Check if second card number in hand matches a card in flop
      flop.cards[0].number = "b"  # Change flop to have a matching number
      flop.numbers = "bde"  # Update numbers accordingly
      hand.cards[0].number = "f"  # Change first card to no match
      hand.numbers = "fb"  # Update numbers accordingly
      result = checkPairs(hand, flop)
      self.assertTrue(result)

      #def test_checkPairs_no_match(self):

      hand.cards[1].number = "g"  # Change hand to have no matching number
      hand.numbers = "fg"  # Update numbers accordingly
      result = checkPairs(hand, flop)
      self.assertFalse(result)

    # def test_checkStraights(self):
    #     # Check if first card number in hand is part of a straight in flop
    #     result = checkStraights(hand, flop)
    #     assertTrue(result)

    # def test_checkStraights_no_match(self):
    #     # hand.cards[0].number = "f"  # Change hand to have no matching number
    #     # hand.numbers = "fb"  # Update numbers accordingly
    #     # result = checkStraights(hand, flop)
    #     # assertFalse(result)
    #     assertFalse(True)

    def test_checkFlushes(self):
      # @TODO use new classes
      hand = {
          "cards": [{"number": "a", "suit": "y"}, {"number": "b", "suit": "y"}],
          "numbers": "ab",
          "suits": "yy"
      }
      flop = {
          "cards": [{"number": "a", "suit": "z"}, {"number": "d", "suit": "y"}, {"number": "e", "suit": "z"}],
          "numbers": "ade",
          "suits": "zyz"
      }

      # suited hand, one on flop
      result = checkFlushes(hand, flop)
      self.assertTrue(result)

      # one flush card in hand, two on flop
      hand.cards[1].suit = "z"  # Change hand to have no matching number
      hand.suits = "yz"  # Update numbers accordingly
      result = checkFlushes(hand, flop)
      self.assertFalse(result)
      
      # suited hand, two on flop
      
      # suited hand, three on flop
      
      # suited hand, none on flop
      

if __name__ == '__main__':
  unittest.main()
