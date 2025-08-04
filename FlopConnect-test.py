import unittest
from FlopConnect import checkPairs, translateCard, checkStraights, checkFlushes, Hand, Flop, Card

class TestFlopConnect(unittest.TestCase):
    def test_checkPairs(self):
        # Check first card in hand matches
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("a", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Check second card in hand matches
        hand = Hand(Card("f", "s"), Card("b", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertTrue(result)

        # Test no match
        hand = Hand(Card("f", "s"), Card("g", "n"))
        flop = Flop(Card("b", "n"), Card("d", "s"), Card("e", "n"))
        result = checkPairs(hand, flop)
        self.assertFalse(result)

    # def test_checkStraights(self):
    #     # Check if first card number in hand is part of a straight in flop
    #     result = checkStraights(hand, flop)
    #     assertTrue(result)

    #     # hand.cards[0].number = "f"  # Change hand to have no matching number
    #     # hand.numbers = "fb"  # Update numbers accordingly
    #     # result = checkStraights(hand, flop)
    #     # assertFalse(result)
    #     assertFalse(True)

    def test_checkFlushes(self):
        # Test suited hand, one on flop matches
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "n"), Card("d", "s"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # Test one suit in hand, two on flop matches
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "n"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # one suit in hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, two on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, three on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "s"), Card("d", "s"), Card("e", "s"))
        result = checkFlushes(hand, flop)
        self.assertTrue(result)

        # suited hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "s"))
        flop = Flop(Card("c", "n"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, one on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "s"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)

        # one suit in hand, none on flop
        hand = Hand(Card("a", "s"), Card("b", "n"))
        flop = Flop(Card("c", "n"), Card("d", "n"), Card("e", "n"))
        result = checkFlushes(hand, flop)
        self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()
